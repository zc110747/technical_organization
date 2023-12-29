#/usr/bin/python3
#本例程用于展示python3的基础语法，包含如下内容
#1. python基本类型
#2. 操作运算符
#3. 字符串处理
#4. 列表和列表处理
#5. 元组和元组处理
#6. 字典和字典处理
#7. 集合和集合处理
#8. Python语句
#9. Python异常处理

import traceback  

#--------------------------------------------------------------------------------
#------------------------------- python基本类型 ----------------------------------
#--------------------------------------------------------------------------------
def type_func():
    """用于处理python基本类型的数据"""
    print(f"----------------{traceback.extract_stack()[-1][2]}-----------------")

    #--------------------- 整型 -------------------
    int_val:int = 4
    print(f"int_val: {int_val}")

    #--------------------- 浮点型 -------------------
    float_val:float = 3.5
    print(f"float_val:{float_val}")

    #--------------------- 复数 -------------------
    complex_val0:complex = complex(3, 4)
    complex_val1:complex = complex(2, 5)
    print(f"complex_val:{complex_val0}, add:{complex_val0+complex_val1}, mul:{complex_val0*complex_val1}")
    print(f"{complex_val0.real, complex.imag}")

    #--------------------- 布尔类型 -------------------
    bool_val:bool = True
    print(f"bool_val:{bool_val}, type:{type(bool_val)}")

    #--------------------- 字符串 -------------------
    str_val:str = "test_str"
    print(f"str_val:{str_val}".title())

    #--------------------- 字符数组 ------------------
    byte_arr:bytes = str_val.encode("utf-8")
    print(f"byte_arr:{byte_arr}, {len(byte_arr)}")
    test_str:str = str(byte_arr)
    print(f"test_str:{test_str}, {len(test_str)}")

#--------------------------------------------------------------------------------
#----------------------------------- 运算符操作 ----------------------------------
#--------------------------------------------------------------------------------
def calc_run():
    """运算符操作说明"""
    print(f"----------------{traceback.extract_stack()[-1][2]}-----------------")

    x = 5
    y = 3
    z = -1 

    #基础 
    #加减乘除 +，-， *， /
    #指数 **
    #取整 //，取余 %
    #取反 -
    print(f"{x+y}, {x-y}, {x*y}, {x/y}, {x**y}, {x//y}, {x%y}, {-z}")

    #绝对值 abs
    #商元组 divmod
    #浮点四舍五入 round
    #幂次 pow(x, y) = x**y pow(x, y, z)= (x**y)%z
    print(f"{abs(z)}, {divmod(x, y)}, {round(x/y)}, {pow(x, y), pow(x, y, y)}")

    #类型转换
    #bin 转换成二进制
    #oct 转换成八进制
    #hex 转换成十六进制
    print(f"bin:{bin(x)}, {oct(x)}, {hex(x)}")

    #int 转换成十进制，支持字符串
    print(f"int:{int(0xf2)}, {int('0xf2', base=16)}")

    #位逻辑运算符
    # | 或运算， & 与运算， ^ 异或运算
    # << 左移，>> 右移， ~取反
    print(f"bit:{x|y}, {x&y}, {x^y}, {x<<1}, {x>>1}, {~x}")

#--------------------------------------------------------------------------------
#----------------------------------- 字符串处理 ----------------------------------
#--------------------------------------------------------------------------------
def str_process():
    """字符串处理实现"""
    print(f"----------------{traceback.extract_stack()[-1][2]}-----------------")
    
    int_val:int = 4

    #字符串的格式化方式
    #1. 使用%类似c的方式替换
    #2. 使用format格式化字符串
    #3. 使用f-string之间替换字符串
    print("value:%d, type:%s"%(int_val, type(int_val)))
    print("value:{0}, type:{1}".format(int_val, type(int_val)))
    print(f"value:{int_val}, type:{type(int_val)}")

    #title 首字符大写字符串
    #lower 小写字符
    #upper 大写字符
    #startswith 以...开头
    #endwith 以...结尾
    str_val:str = "test_str"
    print(f"str_val:{str_val.title(), str_val.lower(), str_val.upper(), str_val.startswith('1'), str_val.endswith('str')}")
    str_val = str_val[:2]
    print(f"str_val:{str_val}")

    #输出包含{}, 需要用{{}}结构
    #format方法操作
    fstr:str = "{{{0}}}, {1}".format("Today", "We stand up!")
    print(fstr)
    fstr = "{who} turned {age} this year".format(who="she", age = 88)
    print(fstr)
    #调用元组的值
    stock = ["paper", "envelopes", "notepads", "pens"]
    fstr = "We have {0[1]} and {0[2]} in shock".format(stock)  
    print(fstr)

    #读取字典的值
    d = dict(animal = "elephant", weight=12000)
    fstr = "The {0[animal]} weights {0[weight]}kg".format(d)
    print("The {animal} weights {weight}kg".format(**d)) #**映射拆分，支持字典内属性直接填充(不过如果不只一个参数传递，映射必须是最后一个)

    #字段名忽略
    fstr="{} {} {}".format("Python", "can", "count")             
    print(fstr)

    #**local引用本地值
    print("Element {int_val}".format(**locals()))

    #综合应用
    #映射必须最后一个，关键字参数who放置在列表参数之后
    #参数顺序: 列表参数，关键字参数，映射
    habit = ["swimming", "dancing", "singing", "running"]
    age = 12
    fimally = dict(father="John", mather="Lily")
    fstr = "{who} is {0} this year, {who} loves {1[0]}, father is {father}, mather is {mather}".format(age, habit, who="Lucy", **fimally)
    print(fstr)

#--------------------------------------------------------------------------------
#-------------------------- 列表(可以包含基础类型的有序集合) -----------------------
#--------------------------------------------------------------------------------
def list_process():
    """列表和功能说明"""
    print(f"----------------{traceback.extract_stack()[-1][2]}-----------------")

    #列表索引从0开始，到len-1, 也可以从-1开始，表示最后一个数据
    list_val:list = [1, "2", 3, "s", 3.5]
    print(f"list_val:{list_val}, {list_val[0]}, {list_val[-1]}")

    #append 在list的尾部插入元素
    #len    获取列表的长度
    list_val.append(True)
    print(f"list val len:{len(list_val)}")

    #insert 在指定位置插入元素
    list_val.insert(0, complex(1, 2))
    print(f"list_val:{list_val}, {list_val[-1]}")

    #del 删除指定位置的list的元素
    del list_val[1]
    print(f"list_val:{list_val}, {list_val[-1]}")

    #pop 删除尾部的元素
    list_val.pop()
    list_val.pop(1)
    print(f"list_val:{list_val}, {list_val[-1]}")

    #remove 根据值删除元素
    list_val.remove(3)
    print(f"list_val:{list_val}, {list_val[-1]}")

    #sort   对列表永久排序
    #sorted 对列表进行临时排序
    #reverse 翻转列表
    list_val.reverse()
    print(f"list_val:{list_val}, {list_val[-1]}")

    #字符串的join方法处理字符数组
    str_list:list = ['h', 'e', 'l', 'l', 'o']
    str_val:str = ''.join(str_list)
    print(f"str_val:{str_val}")

    #截取列表
    str_list0:list = str_list[1:]
    str_list1:list = str_list[:2]
    print(f"str_list0:{str_list0}, {str_list1}")

#--------------------------------------------------------------------------------
#------------------------------- 元组(不可变列表序列)  ----------------------------
#--------------------------------------------------------------------------------
def tuple_process():
    """元组和功能说明"""
    print(f"----------------{traceback.extract_stack()[-1][2]}-----------------")

    #tuple 
    tuple_val:tuple = (1, 2, 3, 4)
    print(f"tuple_val:{tuple_val}, {tuple_val[-1]}, {type(tuple_val), {len(tuple_val)}}")

    #count 返回某个元素出现的次数
    #index 返回指定元素第一次出现的位置
    print(f"tuple_val:{tuple_val.count(1)}, {tuple_val.index(2)}")

    #遍历元组
    for val in tuple_val:
        print(f"{val}", end=" ")
    print("")

    #解包方法
    a, b, c, d = tuple_val
    print(f"{a} {b} {c} {d}")

    #生成新的元组
    tuple_val += (6,)
    print(f"tuple_val:{tuple_val}, {tuple_val[-1]}, {type(tuple_val), {len(tuple_val)}}")

#-------------------------------------------------------------------------
#---------------------------- 字典(存储键值对的基础类型) -------------------
#------------------------------------------------------------------------- 
def dict_run():
    """字典和功能说明"""
    print(f"----------------{traceback.extract_stack()[-1][2]}-----------------")

    #字典类型
    #key可以为所有基础类型(bool型True当成1，False被当成0)
    #value则除了基础类型外，还可以为组合类型(包含可以为另一个字典)
    dict_val:dict = {
        0:"test0",
        1:"test1",
        "2":complex(1, 2),
        complex(1, 2): [1, 2, 3],
    }
    print(f"dict_val:{dict_val}, {type(dict_val)}, {len(dict_val)}")

    #读取遍历
    print(f"{dict_val[0]}, {dict_val['2']}, {dict_val[complex(1, 2)]}")

    #字典增加元素
    dict_val["3"] = "test3"
    dict_val["2"] = "test2"
    del dict_val[1]

    #字典获取指定key的值
    val = dict_val.get(0, "no key in dict")
    print(f"dict_val:{dict_val}, {type(dict_val)}, {len(dict_val)}, {val}")

    #遍历字典
    for key, value in dict_val.items():
        print(f"{key}:{value}", end=" ")
    print("")

    for key in dict_val.keys():
        print(f"{key}", end=" ")
    print("")

    for value in dict_val.values():
        print(f"{value}", end=" ")
    print("") 

    for x, y in (1, 2), (2, 3), (3, 4):
        print(f"{x}:{y}", end=" ")
    print("")        

#-------------------------------------------------------------------------
#--------------------------- set(无序的元素集合) --------------------------
#------------------------------------------------------------------------- 
#集合内每个数据都是独一无二的, 重复数据项添加无意义
#set内元素类型需要支持hash，因此set，list和dict不能作为set的元素(hash不支持)
def set_run():
    """集合和功能说明"""
    print(f"----------------{traceback.extract_stack()[-1][2]}-----------------")

    #创建集合 {}
    #frozenset 冻结的set，不支持更改
    set_val:set = {7, "veil", 0, -29, ("x", 11), frozenset({1, 2}), 2}
    print(f"set_val:{set_val}, {type(set_val)}, {len(set_val)}")
    
    #遍历集合
    for val in set_val:
        print(f"{val}", end=" ")
    print("")

    #add 添加元素
    #pop 弹出set变量
    #isdisjoint 判断两个set是否不相交，所有元素不相同为True，反之False
    #differenct 判断前set不在后set中的对象
    set_val.add(5)
    set_val1 = {1, 4, 8, 7}
    print(f"set_val1:{set_val1}, {set_val1.isdisjoint(set_val)}, {set_val1.difference(set_val)}")

    #intersection 获取交集，生成新的集合，等同于&
    #symmetric_difference 反交集获取不同的值，等同于^
    #issubset   判断是否是子集
    #issuperset 判断是否是超集
    print(set_val.intersection(set_val1), set_val&set_val1, set_val.symmetric_difference(set_val1), set_val^set_val1) #s和s1的交集/反交集
    print(set_val.issubset(set_val1), set_val.issuperset(set_val1))

    #遍历集合，查找指定结尾的数据
    files = {"Index.html", "fRrame.htm", "englisH.html", "jquery.js", "index.css"}
    htmls = {x for x in files if x.lower().endswith((".html", ".htm"))}
    print(htmls)

#-------------------------------------------------------------------------
#----------------------------------语句-----------------------------------
#------------------------------------------------------------------------- 
def statement_run():
    """语句功能说明"""
    print(f"----------------{traceback.extract_stack()[-1][2]}-----------------")

    run_list = [1, "s", 2.5, complex(2, 4)]
    work_list = [2, True, 3.5]

    #in/not in=>bool类型
    in_val0:bool = 1 in run_list
    in_val1:bool = 2.5 not in run_list
    print(f"in_val0:{in_val0}, in_val1:{in_val1}")

    #比较运算符<, >, =, <=, >=, !=
    in_val0 = 2>3
    in_val1 = 3.5<=2.4
    in_val2 = 2!=3
    print(f"in_val0:{in_val0}, {in_val1}, {in_val2}")

    #逻辑运算符and, or, not
    in_val0:bool = 1 in run_list and 2 in run_list
    in_val1:bool = "s" not in run_list or 2.5 in run_list
    in_val2:bool = not 1 in run_list
    print(f"in_val0:{in_val0}, in_val1:{in_val1}, in_val2:{in_val2}")
   
    #分支语句 if...elif...else
    val : int = 2
    if val in run_list:
        print(f"val {val} in run_list")
    elif val in work_list:
        print(f"val {val} in run_list")
    else:
        print("not in all list")

    #==和!=
    if val == 2:
        print(f"val equal {val}")


    #循环语句for...in...
    #range生成整数序列
    if run_list:
        for val in run_list:
            print(f"{val}", end=" ")
    else:
        print("run list is empty!")
    print("") 

    for index in range(0, len(run_list)):
        print(f"{run_list[index]}", end=" ")
    print("") 

    #循环while语句
    i = 0
    while True:
        if(i >= len(run_list)):
            break
        print(f"{run_list[i]}", end=" ")
        i += 1
    print("") 

    #is 判断是否引用同一对象
    a = ["retention", 3]
    b = ["retention", 3]
    c = a
    print(f"{a is b}, {c is a}, {a is not None}")

#-------------------------------------------------------------------------
#-------------------------------异常处理-----------------------------------
#------------------------------------------------------------------------- 
def exception_run():
    try:
        divisor = 10
        indata = 0
        print(divisor/indata)
    except ValueError as err:
        print(err)

if __name__ == '__main__':
    #基础类型
    type_func()

    #字符串处理
    str_process()
    
    #运算符
    calc_run()

    #列表类型
    list_process()

    #元组类型
    tuple_process()

    #字典类型
    dict_run()

    #集合类型处理
    set_run()
    
    #逻辑语句
    statement_run()

    #异常运行
    #exception_run()