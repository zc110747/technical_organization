#!/usr/bin/env python3

import sys
import string

#if/if not...elif...else 条件分支语句
offset = [0, 0]
if sys.platform.startswith("win"):
    offset[0] = 10
offset[1] = 20 if not sys.platform.startswith("win") else 10 
print(offset)

#擅用圆括号规避陷阱
margin = False;
width = 100 + (10 if margin else 0)
print(width)

#while bool_express:
#   suite
#else:
#   suite
def list_find(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index+=1
    else:
        index = -1
    return index

lst1 = ["a", 'b', 'c']
print(list_find(lst1, 'a'))

#for...in...迭代
#continue/pass 跳过本次循环
#break  终止循环
for val in lst1:
    print(val, end=" ")
else:
    print("")

#异常处理
#try...except...
#Exception
try:
    x = lst1[5]
except LookupError:
    print("Lookup error occurred")
except KeyError:
    print("Invalid key used")

def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="utf-8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except  (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()

    return lines

print(read_data('out.txt')); #['alpha bravo charlie\n', 'asddasdada\n', '11111111111111\n', 'sdsadadsa']

class FoundException(Exception):pass
def define_except(table, target):
    try:
        for row, record in enumerate(table):
            for column, field in enumerate(record):
                for index, item in enumerate(field):
                    if item == target:
                        raise FoundException()
    except FoundException:
        print("found at ({0},{1},{2})".format(row, column, index));
define_except(["1", "2"], "2");

#自定义函数
#局部函数/Lambda函数
#参数语法不允许有默认值参数后面有无默认值参数
def letter_count(text, letters = string.ascii_letters):
    letters = frozenset(letters)
    count = 0
    for char in text:
        if char in letters:
            count += 1
    return count
print(letter_count("string"))

def append_if_even(x, lst = None):
    lst = [] if lst is None else lst
    if x%2 == 0:
        lst.append(x)
    return lst
print(append_if_even(2, [2, 3, 5])) #[2, 3, 5, 2]

def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result
print(product(1, 2, 3, 4))