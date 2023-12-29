#usr/bin/python
#处理说明
#flv.py 不带参数
#处理当前文件夹下的所有FLV文件, 提取aac音频

#flv.py xx.flv xx.flv......
#处理所有标注的flv文件

import sys
import os
from flv import CreatObj

def file_manage(path):
    Obj = CreatObj(path)
    if Obj["format"] == "flv":
        print("Process file: {0}".format(path))
        Obj["video"].Parser()
    else:
        print("Invalid file: {0}".format(path))

if len(sys.argv) == 1:
    CurrentPath = os.path.split(os.path.realpath(__file__))[0];

    #获得当前文件夹下所有的文件(Python文件除外 排除.py)
    pathlist = [os.path.join(CurrentPath, filename) 
                    for filename in os.listdir()
                        if filename.split('.')[-1] != 'py' and os.path.isfile(filename)]

    for path in pathlist:
        file_manage(path)
    os.sy

else:
    for path in sys.argv[1:len(sys.argv)]:
        file_manage(path)