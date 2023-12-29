#Study.py
#代码通过用缩进对齐来表示代码逻辑

#模块化导入
import sys
import os

sys.stdout.write("Sys Test!\n");
print(sys.version)

#函数功能
def printf(str='no input!'):
    print(str)

#函数参数可以设置默认值
printf()
printf("Function Test!") 

#对于python语言, 双引号和单引号没有区别
mystring = 'Str Test'
printf(mystring);

printf("%s is equal useful as %s"%("Python", "C++")) # %实现字符串替换

def mkdir(path):
    path=path.strip()
    isExists=os.path.exists(path)
 
    #判断文件夹是否存在，不存在则创建
    if not isExists:
        os.makedirs(path)
        print(path+' 创建成功')
    else:
        pass
    return path

inpath = os.path.split(os.path.realpath(__file__))[0];
inpath = mkdir(inpath+"\\base");
#2.x print>> -> print(str, file=...)
logfile = open(inpath+"/"+"test.txt", 'w')  #将信息导入文件
print(mystring, file=logfile)
logfile.close();

def printf_abs(num):
    printf(abs(num))
printf_abs(-10)

#运算符
#四则运算 优先级(优先级逐渐提高)
#1. **(乘方)  
#2. + -（正负号) 
#3  * / // %(乘 除 浮点除) 
#4  + -(加 减)
#比较符
# > < == !=
#逻辑运算符
#and or notnit
printf(-2*3 + 4/2 + 6.0//3.1 + 3**2) #(-6 + 2 + 1 + 9) = 6.0

#Decimal 
from decimal import *
c = getcontext()
print(c)
a= Decimal(100)
print(a)

#字符串 正数表示从字符串首位计算(0是开始) 负数表示从尾计算(-1是末尾)
#n:m    表示从n到m-1的字符，可省略(在前表示从0开始，在尾表示到末尾结束)
pystr = 'string Test'
printf(pystr[0]+':'+pystr[-3]+':'+pystr[1:4]) #s:e:tri
printf(pystr[:2]+':'+pystr[2:]) # st:ring:Test

#列表
#和字符串类似
pylist = [1, 2, 3, 4]
printf(pylist[0]+pylist[-1]) 
printf(pylist[0:4])

#元祖
pyarray = (1, 'array', 'test', 2)
printf(pyarray[:3])

#字典
#类似javascript的对象
adict = {
    'name': 'bob',
    'age' : 80,
    'work' : 'enginerr'
}
printf(adict['name'])

#循环 while/for
num = 0
while num<len(pyarray):
    print(pyarray[num], end=' ')
    num+=1
print()
for item in pylist:
    print(item, end=' ')
print()
for item in adict:
    print("%s:%s"%(item, adict[item]), end=' ')
print()

#range 只能输入整数
#enumerate 运行同时遍历元素和索引
for item,data in enumerate(range(1, 5)):
    print("%d(%d)"%(item, data), end=" ")
print()

#遍历对象的结构不符合实际顺序？(目前看因为hash值来判断顺序)
for item,string in enumerate(adict):
    print("%s:%s"%(item, string), end=" ")  
print()

sqddata = [x**2 for x in range(10) if not x%2]
for i in sqddata:
    print(i, end=" ")
print()

#此时修改pylist会导致MList的改变, 表示pylist和Mlist引用同一个对象，这是很危险的
MList = [1, pylist, 3]
print(MList)                #1 1 2 3 4 3
pylist[0] = 0               
print(MList)                #1 0 2 3 4 3
#通过副本隔离，不在引用同一对象
segreList = [1, pylist[:], 3]
print(segreList)            #1 0 2 3 4 3
pylist[0] = 1
print(segreList)            #1 0 2 3 4 3

#类的实现 __init__相当于构造函数
class person(object):
    version = 0.1
    def __init__(self, nm='bob'):
        self.name = nm
    def show(self):
        printf(self.name)

someone = person();
someone.show();
otherone = person('lucy');
otherone.show();

#2.x raw_input -> 3.x input
user = input('String you want:')
printf("you input is %s"%user)
