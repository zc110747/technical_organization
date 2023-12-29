#/usr/bin/python3
#本例程用于描述常用模块的功能，特别是内置模块功能
#random:随机数模块
import random
import math
import traceback  

def module_simple():
    """用于处理python基本类型的数据"""
    print(f"----------------{traceback.extract_stack()[-1][2]}-----------------")

    #------------------------ random ---------------------
    #random 生成0~1之间的随机数
    #randint 生成指定范围的整数随机整数
    #rrange 生成指定范围满足指定步长的整数
    rval:float = random.random()
    rint:int = random.randint(5, 1000)
    rrange:int = random.randrange(0, 1000, 5)
    print(f"{rval}, {rval*1000}, {rint}, {rrange}")

    #shuffle 随机打乱序列内数据
    #choice 随机选择序列中的对象
    #choices 根据权重选择序列中的多个对象
    #sample 随机选择k个序列中的不重复对象
    list_val:list = [2, 15, (1, 2), 15, "str"]
    random.shuffle(list_val)
    print(f"{random.choice(list_val)}, {list_val}, {random.choices(list_val, weights=None, cum_weights=None, k=2)}, {random.sample(list_val, 2)}")

if __name__ == "__main__":
    
    #简单模块
    module_simple()