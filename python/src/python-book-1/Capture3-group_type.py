#!/usr/bin/env python3

import collections
import copy

#元组 在创建后是固定的, 不支持方法修改(拼接是创建新的副本)
hair = "black","brown","blonde","red"
print(hair[-3:], *hair)               #元组支持字符串的任意截取，同时用*可以读元组里的每个变量
hair = hair[:2] + ("gray",) + hair[2:]
print(hair)
print(hair.__hash__())                #元组支持hash方法

for x,y in (1, 1), (2, 4), (3, 9):
    print(x, y, end=" ")
print("")

things = (1, -7.5, ("pea", (5, "Xyz"), "queue"))
print(things[2][1][1][2])

#列表 列表是包含0~多个对象引用的有序序列
#列表支持任意index截取, 同时用*也可以取列表里的每个参数
L = [6, 1, 2, 3, 5]
print(L[1:-1], *L[1:])              

#*取的参数可直接由函数调用
def listproduct(a, b, c):
    return a*b*c
print(listproduct(L[0], *L[3:]))    

#排序, 并输出 for...in...取每个参数
l = sorted(L)
for data in l:
    print(data, end=" ")            
print(":l-sort")

#反转
lr = l[::-1]
print(lr, ":l-reversed")


#输出，利用range取每个index, 再输出
for i in range(len(L)):
    print(L[i], end=" ")            
print(":L-range")
L = l[:1] + ["inline",] + l[1:]
for i in range(len(L)):
    print(L[i], end=" ")          
print(":L+")

#列表添加/删除末尾
L.extend(["tail1"])
L += ["tail2"]
L.extend(["extratail"])
print(L)
L.pop()
print(L)

#insert 在指定索引位插入对象
l.insert(1, "add")
l.insert(0, ["head"])
l[2:2] = ["add2"]
print(l)                #[['head'], 1, 'add2', 'add', 2, 3, 4, 5, 6]

#基于索引的单个/分片替换/删除
l[0][0] = "change"
l[1:3] = [3, "2"]
print(l)                #[['change'], 3, '2', 'add', 2, 3, 5, 6]

l[2:4] = []             
#del l[2:4]
print(l)                #[['change'], 3, 2, 3, 5, 6]

#步距的运用
l[1::2] = [0]*len(l[1::2])
print(l)                #[['change'], 0, 2, 0, 5, 0]
print(l[::-1])          #[0, 5, 0, 2, 0, ['change']]

leaps = []
for year in range(1900, 1940):
    if(year%4==0 and year%100 != 0) or (year%400 == 0):
        leaps.append(year)
print(leaps)

#使用列表内涵创建列表(任何列表内涵都可通过for...in重写)
leaps = [y for y in range(1900, 1940)
            if(y%4==0 and y%100 !=0) or (y%400 == 0)]
print(leaps)
codes = [s+z for s in  "SF" for z in "THLB"
            if not(s=="S" and z=="B")]
print(codes)

#set 集合类型 0或多个对象引用的无序组合
#内置的list, set, dict都不支持hash运算，因此不能添加到集合中
#集合内每个数据都是独一无二的, 重复数据项添加无意义
#frozeset固定集合
s = {7, "veil", 0, -29, ("x", 11), frozenset({1, 2}), 2} 
print(s, frozenset(s).__hash__())
for sdata in s:
    print(sdata, end=" ")
print("")

#空列表用set()创建, 因为{}代表空的字典
s1 = set({1, 2, 7})
s1.add(5)             #将数据项添加到集合中
print(s1, len(s1))
print(s.difference(s1), s-s1)   #difference 返回一个包含在s但不在s1中的集合 

#移除set中的某项/随机一项 
print(s1.remove(1), s1)         #s1.discard(1) 无返回值
print(s1.pop(), s1)             #s1位空触发KeyError
print(s1.isdisjoint(s1))        #False 判断两个set是否有相同项
print(s.intersection(s1), s&s1, s.symmetric_difference(s1), s^s1) #s和s1的交集/反交集
print(s.issubset(s1), s.issuperset(s1)) #False False 子集/超集

#set没有重复的变量，可以用于网页ip/url提取之后的处理
#set可接受元组, 列表, 集合类型，并转换成set类型
ips = ("192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.2")
for ip in set(ips):
    print(ip)

#集合内涵
files = {"Index.html", "fRrame.htm", "englisH.html", "jquery.js", "index.css"}
htmls = {x for x in files if x.lower().endswith((".html", ".htm"))}
print(htmls)

#dict映射类型
#字典的初始化和创建
#d1 = {"id":1948, "name":"washer", "size":3}
#d1 = dict({"id":1948, "name":"washer", "size":3})
#d1 = dict(id=1948, name="washer", size=3)
#d1 = dict([("id", 1948), ("name", "washer"), ("size", 3)])
d1 = dict(zip(("id", "name", "size"), (1948, "washer", 3)))
print(d1)
d1["id"] -= 1
d1["usr"] = "army"  #向字典里添加项
print(d1)

del d1["name"]      #从字典删除项 del equal d1.pop("name", v)  
# d1.popitem()      #随机删除一项
print(d1)

#字典创建，默认初始化为None或者value
d2 = dict.fromkeys(('id', "name", "size"), 0)
print(d2)

# for key in d2:
#       if d1.get(key) != None:
#         d2[key] = d1.get(key)
for key in d2:
    if key in d1.keys():       #d.keys()获得所有的键值
        d2[key] = d1.get(key)  #d.get(k, v) equal d[k]  但兼容性更好 失败会返回v
print(d2)
print(d2.setdefault("updata", "now"), d2) #等同于get, 但如果不存在会将键插入字典中

#字典的键视图和值视图
print(d2.items(), d2.values())
for key, value in d2.items():
    print(key, value)

#字典内涵
d3 = {k:v for k,v in d2.items() if len(k) > 3}
print(d3)

#默认字典 不会产生keyError, 当项不存在时，直接创建
words = collections.defaultdict(int)
x = words["first"]
print(words)

#有序字典
d4 = collections.OrderedDict([('z',-4), ('e', 19), ('k', 7)])
print(d4, d4.keys(), d4.values())
tasks = collections.OrderedDict();
tasks[0] = "Backup"
tasks[2] = "Scan Email"
tasks[1] = "Build System"
print(tasks)
out = tasks.popitem(last=False)  #从有序字典里删除一项 空为末尾
tasks[out[0]] = out[1]
print(tasks)

#组合类型的迭代和复制
def CompositeTypes():
    for i in [1, 2, 4, 8]:
        print(i, end=" ")
    print("")

    #显示迭代子
    i = iter([1, 2, 4, 8])
    while True:
        try:
            print(next(i), end=" ")
        except StopIteration:
            break;

    songs = ["Because", "Boys", "Carol"]
    beatles = songs          #指向同一引用,一个修改，另一个也修改
    print(songs, beatles)
    beatles[2] = "Cayenne"
    print(songs, beatles) 
    beatles = songs[:]      #复制，互不干扰 
    beatles[2] = "Carol"     
    print(songs, beatles)

    x = [53, 68, ["A", "B", "C"]]
    y = x[:]            #浅拷贝, 基础类型一致，组合类型绑定
    print(x, y)
    y[2][0] = "Q"
    print(x, y)
    y = copy.deepcopy(x) #深拷贝, 完全分离
    y[2][0] = "A"
    print(x, y)  
CompositeTypes();