# 综述
对于单片机来说，IAP(又称在应用编程)就是不需要使用调试工具如jlink，st-link, 通过芯片自带的外部接口如USART，USB，CAN或ETH接口实现的远程下载功能。因为工作的需求，也实现了各种不同的远程升级方案，也遇到各种问题，这里整理总结下，并实现一种我结合实践中最后使用的方案，以后遇到也有帮助。<br />
# IAP实现原理
IAP的实现包含协议通信和FLASH擦除下载，应用跳转和中断管理，其中协议和FLASH部分属于基础，应用跳转很多人都使用跳转命令，不过不理解背后的原理，而跳转后和跳转前的中断处理又是IAP完成后的经常遇到的问题，下面从原理上解释流程，可以帮助分析和实现IAP功能。<br />
## IAP应用跳转
在了解IAP的跳转之前，先要了解ARM芯片的启动过程，以我目前使用STM32芯片的为例，在"存储器和总线架构>启动配置"章节说明, 在系统复位后，根据Boot1和Boot0两个引脚选择可以从不同的存储区域启动，以Boot0=0, 从主闪存存储器为例，包含以下步骤。 <br />

1. 主闪存存储器被映射到启动空间(0x0000 0000)，实际地址0x08000000。<br />
2. 从偏移0的地址取出1字的数据，赋值给MSP，里面保存的是堆栈的起始地址。<br />
3. 从偏移4的地址取出1字的数据，赋值给PC，里面保存的是ResetHandler的地址。<br />

在PC被赋值后，就执行下一步函数调用，进入ResetHandler入口，在有了执行地址和堆栈起始地址后，应用便拥有开始执行的所有条件。至于这部分内容是由内核规定的，在代码中由启动文件的中断向量表实现，例如startup_stm32fxxx.h中的__Vectors定义。<br />
```s
__Vectors       DCD     __initial_sp               ; Top of Stack
                DCD     Reset_Handler              ; Reset Handler
```
中断向量表就放置在编译后固件的起始位置，bootloader到APP的跳转就是在代码中模拟该过程，这里还有C语言的技巧，利用函数指针调用函数。<br />
```c
typedef  void (*pFunction)(void);

void test_func(void)
{
}

int main(void)
{
    uint32_t func_addr;

    pFunction func = test_func;
    func(); //此时可以调用test_func.
    
    //如果知道函数的地址(必须32位系统，64位系统使用uint64_t)
    func_addr = (uint32_t)test_func;
    func = (pFunction)func_addr;
    func();

    return 0;
}
```
如果我们本身已经知道test_func的地址，则可以直接使用类型((pFunction)0x080001e1)()格式调用，基于芯片flash中数据的存储信息和C语言的函数指针的机制，跳转程序就基于此实现，适用于基本全部的32位Cortex-M的芯片。<br />
```c
#define APPLICATION_ADDRESS         0x08010000                      //应用起始地址
#define APP_MSP_ADDRESS             (APPLICATION_ADDRESS)           //内部保存MSP地址
#define APP_RUN_ADDRESS             (APPLICATION_ADDRESS+4)         //内部保存应用的ResetHandler地址
typedef  void (*pFunction)(void);

int IAP_RunApp(void)
{
    pFunction JumpToApplication;
    uint32_t JumpAddress;

    //检测APP的起始位置是否正确
    //起始地址是MSP的地址，以RAM 64K为例，所以地址不可能超过0x20010000，和0x2FFE0000与一定是0x20000000
    //不同容量RAM需要修改这个匹配值，如RAM 256K为例0x2FF80000
    if(((*(__IO uint32_t*) APP_MSP_ADDRESS)&0x2FFE0000) == 0x20000000)
    {
        //将所有模块复位，在下章说明
        ResetToDefault();

        //设置MSP的地址
        __set_MSP(*(__IO uint32_t*) APP_MSP_ADDRESS);

        //取出需要跳转的地址
        JumpAddress = *(__IO uint32_t*)APP_RUN_ADDRESS;

        //执行跳转命令
        JumpToApplication = (pFunction)JumpAddress;
        JumpToApplication();
        return 0;
    }
    else
    {
        return -1;
    }
}
```
## 跳转问题分析
对于很多做IAP开发的，往往遇到升级成功后，跳转后死机，然后重启后下次执行又能够正常执行，大部分情况没有问题，但某些情况又偶发性的带来异常，导致产品不稳定，很多人就一劳永逸，下载完成后直接复位，看起来又解决了问题，不过很少去从原理上去关注，当然这方面的资料也很少，因此我根据自己的经验，来解释发生的原因和避免的的方法。当然嵌入式系统往往不是单纯的软件问题，芯片，晶振，外部器件，电源都可能带来上述问题，这里只是个思路，不要将自己局限，在出现问题时抱着怀疑的态度对待系统的任何一个部分，才能更快的找到真正原因。<br />
在上节讲过，我们从bootloader跳转到Application是模拟了系统上电复位的过程实现跳转，但事实上还有一部分是缺少的，这也是跳转后出现问题的主要原因。如果看过参考手册，就可以知道，每个寄存器都有一个上电复位值，在上电复位的过程中，会同时把外设的寄存器设置为默认值，在这种情况下，外设模块的功能往往都是默认关闭的。这就保证了芯片在启动后，不会出现预期外工作的外设模块。<br />
对于Application来说，如果只使用的上述跳转代码，因为未对模块进行处理，那对于bootloader使用的模块，在Application中是保持同样开启和正常配置，这样工作的模块就是非预期的，特别在bootloader中使用的中断，更容易出现问题。<br />

1. 外设仅在bootloader中使用，那么Application没有相应的处理函数，硬件还是会相应触发，但没有相应的软件处理，就会卡死到启动文件或者直接触发hardfault。<br />
2. 外设在bootloader和Application都有使用，是否就没问题，也不一定，因为在进入Application时，在调用初始化之前，某些中断就可能已经触发了，如果中断函数中执行的某些数据需要初始化后执行才正确，那么这就可能应用在启动后工作就异常了(非bootloader开发也要考虑这个问题，数据要在硬件模块配置开始前完成初始化，特别涉及中断的问题)，而且因为触发条件严苛，往往在量产大批量应用时很小几率出现，反而是更难解决的问题。<br />

看到这，是不是有点慌了，IAP有这么多的风险，那么有没有比较简单的办法解决了，当然有，既然我们跳转是模拟上电复位，那把上电复位关于模块寄存器的复位也模拟就可以了，把中断控制位和状态位也清除掉，同样可以干净的跳转到Application中，这样不会出现非预期执行了。这里就利用了RCC模块的RST时钟信号控制了，以我们在Bootloader中使用过UART，Timer1，GPIOA为例，在执行JumpToApplication前，把模块复位，关闭中断就可以。当然HAL库也封装了RST对应的宏，如果使用了其它外设，在下面中添加相应模块复位即可，使用标准库，也有相应的函数进行处理，这种方法也是从原理上最简单也最可靠的规避掉跳转问题的方法，保证Application的执行行为和上电复位一致。
```c
void ResetToDefault(void)
{
    int i;

    //复位GPIO, Timer1和Usart1的时钟
    __GPIOA_FORCE_RESET();
    __TIM1_FORCE_RESET();
    __USART1_FORCE_RESET();

    //释放复位时钟
    __GPIOA_RELEASE_RESET();
    __TIM1_RELEASE_RESET();
    __USART1_RELEASE_RESET();

    //将中断使能为设置为默认值
    for(i = 0; i < 8; i++) 
    {
        NVIC->ICER[i] = 0xFFFFFFFF; // 关闭中断
        NVIC->ICPR[i] = 0xFFFFFFFF; // 清除中断标志位
    }
}
```
这里抛砖引玉，从上电复位机制引申到如何实现应用内跳转，以及如何解决跳转后异常行为的方法，那么在下一篇则基于应用需求，讲述IAP的下载，校验和数据存储机制，并分几类讲解IAP的实现。