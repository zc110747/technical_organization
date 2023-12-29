#!/usr/bin/env python3
import random   #随机数模块
import math
import sys
import decimal
import re

def DataType():
    
    #标识符
    for _ in (0, 1, 2, 3):
        print(_, end=' ')
    print('')

    #随机数, abs
    r = abs(random.randint(-10, 10))
    print(r)

    #浮点型
    π = math.pi;
    print(π*r*r)

    #整型
    x = 10
    y = 8
    z = 3
    #运算符
    print(x+y, end=" ")            #x与y相加   18
    print(x-y, end=" ")            #x与y相减   2
    print(x*y, end=" ")            #x与y相乘   80
    print(x/y, end=" ")            #x与y相除,总是产生浮点数 1.25
    print(x//y, end=" ")           #x与y相除,取整数部分     1
    print(x%y, end=" ")            #x除以y,取余数部分       2
    print(x**y, end=" ")           #x的y次幂                100000000
    print(-x, end=" ")             #取反                    -10
    print(+x, end=" ")             #不做操作                10
    print(abs(x), end=" ")         #取绝对值                10
    print(divmod(x, y), end=" ")   #x除以y，获得商和余数的二元组  (1, 2)
    print(pow(x, y), end=" ")      #x的y次幂                100000000
    print(pow(x, y, z), end=" ")   #相当于(x**y)%z          1
    print(round(x/y, 1))           #返回浮点数四舍五入后得到的相应数  1.2

    #类型转换
    print(bin(x), end=" ")             # '0b1010' 二进制以0b开头  0o, 0x
    print(zfill(hex(x), 4), end=" ")   # '0xa'    十六进制以0x开头
    print(eval(hex(x)), end=" ")       #  10      等同于int，不过容易出漏洞
    print(int(x/y), end=" ")           #  1       将对象转换成整数,去除小数部分
    print(int('0xf1', 16))             #  241     将字符串转换成整数

    #位逻辑操作符
    print(x|0x03, end=" ")         #逻辑或运算     11
    print(x^y, end=" ")            #逻辑异或运算   2
    print(x&y, end=" ")            #逻辑与运算     8
    print(x<<1, end=" ")           #左移一位       20
    print(x>>1, end=" ")           #右移一位       5
    print(~x)                      #取反每一位     -11(补码 取反+1)

    #布尔型
    t = True
    f = False
    print(t and f, t or f)

    #浮点型
    print(equal_float(3.0000000000000001, 3.0))
    s = 14.25.hex()
    f = float.fromhex(s)
    t = f.hex()
    print(s, f, t)

    #math模块支持的方法
    print(math.hypot(3,4), end=" ")   #5.0        根号x平方加y平方
    print(math.frexp(1.5), end=" ")   #(1, 0.5)   取浮点数的整数和小数部分
    print(math.e, end=" ")            #2.718..    返回e的值
    print(math.exp(2), end=" ")       #7.38...    返回e的n次幂
    print(math.floor(1.5), end=" ")   #1          返回小于等于的最大整数
    print(math.pow(1.5, 3), end=" ")  #3.375      返回浮点数的n次幂
    print(math.pi)                    #3.14159..  π的值

    #复数
    z = -2.5 + 3j
    print(z.real, z.imag, end=" ")    #-2.5 3     获得复数的实部和虚部
    print(z.conjugate())              #-2.5-3j    共轭复数

    #十进制数字
    a = decimal.Decimal(1)
    b = decimal.Decimal(2.133123551515)
    print(a+b)

    #字符串
    print(ord('n'))      #获得字符的Unicode
    
    #插入, 截取
    hstr = "hello world!"
    print(hstr[1:7], "!" ,hstr[:-1])          #ello w ! hello world
    
    #比较 < <= == != > >=
    print('ab' > 'ba')                        #false

    #分片
    print(hstr[::2], hstr[::-2])              #hlowrd drwolh

    #字符串方法
    print(hstr.capitalize())            #Hello world!   返回字符串副本，并大写第一个字符
    print(hstr.center(14, 'c'))         #cHello world!c 设定字符串的总长度，不满足则填充指定字符
    print(hstr.count('l', 1, 5))        #2 统计子字符串在字符串指定范围内出现的次数

    #byte流
    byte = hstr.encode("utf-8")
    print(type(byte), byte)             #<class 'byte'> b'hello world!'根据编码类型,将字符串解码为流bytes
    str0 = byte.decode("utf-8")         
    print(str0)                         #hello world! 将文件流解码为指定格式字符串
    
    #str方法
    print(str0.islower(),str0.isupper())#True False 判断字符串至少有一个大写或者小写
    arr = {"a", "B", "c"}
    print("1".join(arr))                #a1B1c 用于其它类型的组合    
    print("1".join(arr).lower()) 
    print("1".join(arr).upper())        #字符串的大小转换
    print(str0.replace("world", "everyone")) #字符串替换,
    print(str0.split(" "))              #字符串分割
    print(str0.zfill(15))               #字符串填充   
    print("*1"*5)                       #字符串复制
    print(strzfill('0x1', 2, 2))        #字符串任意位置填充

    #format字符串格式化
    fstr = "The novel '{0}' was published in {1}".format("Hard Time", 1854)
    print(fstr)
    #被格式化对象包含{},需要复写(类型\\)
    fstr = "{{{0}}}, {1}".format("Today", "We stand up!")
    print(fstr)
    #字段名
    fstr = "{who} turned {age} this year".format(who="she", age = 88)
    print(fstr)
    fstr = "The {who} was {0} last week".format(12, who="boy", )   #关键字参数需要放在列表参数之后
    print(fstr)
    stock = ("paper", "envelopes", "notepads", "pens")             #stock = ["paper", "envelopes", "notepads", "pens"]
    fstr = "We have {0[1]} and {0[2]} in shock".format(stock)      #字段名引用集合或者元组类型
    print(fstr)
    d = dict(animal = "elephant", weight=12000)
    fstr = "The {0[animal]} weights {0[weight]}kg".format(d)
    print("The {animal} weights {weight}kg".format(**d))           #**映射拆分，支持字典内属性直接填充(不过如果不只一个参数传递，映射必须是最后一个)
    print(fstr)
    fstr = "math.pi == {0.pi} sys.maxunicode={1.maxunicode}".format(math, sys) #可以引用导入的模块列表
    print(fstr)
    fstr="{} {} {}".format("Python", "can", "count")              #字段名忽略，高于3.0可用
    print(fstr)
    element = "silver"
    number = 47
    print("Element {number} is {element}".format(**locals()))    #**locals引用局部变量
    #列表参数>关键字参数>映射拆分
    
    habit = ["swimming", "dancing", "singing", "running"]
    age = 12
    fimally = dict(father="John", mather="Lily")
    fstr = "{who} is {0} this year, {who} loves {1[0]}, father is {father}, mather is {mather}".format(age, habit, who="Lucy", **fimally)
    print(fstr)

    #s 用于强制字符串先是 r用于强制表象现显示 a用于强制表象形式，仅适用于ASCII字符
    print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("93.4")))


def strzfill(istr, index, n):
    return istr[:index] + istr[index:].zfill(n)

def equal_float(a, b):
    return abs(a - b) <= sys.float_info.epsilon

#对于bin, hex, oct转换的字符串补0
def zfill(data, n):
    if len(data) > n:
        return data
    else:
        i = 0
        total = n - len(data)
        add = ""
        for i in range(total):
            add += "0"
            
        return data[:2] + add + data[2:]

DataType();