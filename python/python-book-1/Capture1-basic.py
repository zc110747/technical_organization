#!/usr/bin/env python3
import os

print("hello world!")       # hello world!

print(os.getppid())

byte = "hello world"[4]
print(byte)                 # o

str1 = int("45")
int1 = str(912)
print(type(str1), ": ", str1)
print(type(int1), ": ", int1)

#tuple元组数据类型
countries = ("China", "England", "America")
print(countries, " len: ", len(countries))
countries += ("Japan",)
print(countries)

#list列表数据类型
li = ['alpha', 'bravo', 'charlie']
print(li)
li.append('delta')
print(li)
list.append(li, "frame")
li += ["echo"]
print(li, " len: ", len(li))
print(li[3:])               #截取指定字段
print(" ".join(li))         #指定字符串合并

#运算符
# is 判断对象是否引用同一个对象
a = ["retention", 3]
b = ["retention", 3]
c = a
print(a is b, c is a, a is not None)        #False True True

#比较运算符 <, >, =, <=, >=
a = 2
b = 6
c = 4
print(a<b, a>c, a<=c<=b)                    #True Flase True

#成员操作符 in, not in
li = ['alpha', 'bravo', 'charlie']
print("alpha" in li, "above" not in li)    #True True

#逻辑运算符 and, or, not  
#布尔上下文中返回对应True/False, not只返回bool
five = 5
two = 2
zero = 0
print(five and two, two and five, five and zero, two or zero, not zero) #2 5 0 2

#控制流语句
if five < 10:
    print("small")
elif five < 100:
    print("medium")
else:
    print("large")

i = 0
while True:
    if i >= len(li):
        print('')
        break
    item = li[i]
    i+=1
    print(item, end=' ')

#for...in语句
for country in countries:
    print(country, end=' ')
print('')

#基本异常处理
# while(True):
#     line = input("integer: ")
#     if line:
#         try:
#             divisor = 10
#             indata = int(line)
#             print(divisor/indata) 
#         except ValueError as err:
#             print(err)
#             continue
#     else:
#         break
line = input("integer: ")
if line:
    try:
        divisor = 10
        indata = int(line)
        print(divisor/indata)
    except ValueError as err:
        print(err)
else:
    print("Empty Command!")

#函数的创建和调用
import os
def file_write(path):
    outfile = open(path + "/" + "out.txt", "w", encoding="utf-8")
    outfile.write(" ".join(li))
    outfile.close()
inpath = os.path.split(os.path.realpath(__file__))[0];
file_write(inpath)

