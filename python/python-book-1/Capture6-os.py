#!/usr/bin/env python3

import os
import sys

os.chdir("D:\\")

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT)

# 获取以上文件的对象
fo = os.fdopen(fd, "w+")

# 获取当前文章
print("Current I/O pointer position :%d" % fo.tell())

# 写入字符串
fo.write( "Python is a great language1.\nYeah its great!!\n");

# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print("Read String is : ", str)

# 获取当前位置
print("Current I/O pointer position :%d" % fo.tell())

# 关闭文件
os.close( fd )

print("关闭文件成功!!")
