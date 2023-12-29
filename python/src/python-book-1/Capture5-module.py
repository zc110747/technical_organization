#!/usr/bin/env python3

#导入模块
#import importable
#import importable1, importable2...
#对导入模块命名
#import importable as preferred_name  
#从模块中导入对象
#from importable import object
#from importable import object1, object2...
#from importable import *

import os

#获得当前路径
path = os.path.split(os.path.realpath(__file__))[0];
print(path);

