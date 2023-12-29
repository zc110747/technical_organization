#/usr/bin/python

import os
import sys
import functools

type_file = ["bmp"]

def ShellProcess(py, inpath, outpath):
    Command = "{0} {1} {2}".format(py, inpath, outpath)
    os.system(Command)
    
def ImageProcess(py, path):
    global type_file
    for filename in os.listdir(path):
        if filename.split('.')[-1] in type_file:
            ShellProcess(py, filename, "{0}.{1}".format(filename.replace('.', '_'), "c"))
            
#在指定位置填充0
def strzfill(istr, index, n):
    return istr[:index] + istr[index:].zfill(n)
    
#将文件以二进制读取, 并转化成数组保存
def FileHex(inpath, outpath):
    i = 0
    count = 0
    a = []
    b = []
    c = ''
    inf = open(inpath, 'rb');
    outf = open(outpath, 'w')
    bytes_read = inf.read(26);

    if bytes_read[0] != 0x42 and bytes_read[0] != 0x4d:
        print("Invalid BMP File!")

    cnbytes = int.from_bytes(bytes_read[10:14], byteorder='little');
    width = int.from_bytes(bytes_read[18:22], byteorder='little');
    height = int.from_bytes(bytes_read[22:26], byteorder='little');
    inf.read(cnbytes-26);
    
    #偏函数迭代器
    records = iter(functools.partial(inf.read, 1), b'')
                          
    for r in records:
        r_int = int.from_bytes(r, byteorder='big')  
        a.append(strzfill(hex(r_int), 2, 2))
        count += 1

    count = height*width
    for co in range(0, height):
        b += a[(count-width*(co+1)):(count-width*co)]
    
    for ch in b:
        c += ch + ", "
        i += 1;
        if i == 16:
            c += '\n';
            i = 0;   
               
    Name = "bmp";
    a = "static const char " + Name + "["+ str(count) +"]={\n" + c + "\n};\n\n" 
    
    outf.write(a)
    inf.close()
    outf.close()
    return True

#获得当前路径
pyfile = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
length = len(sys.argv)
path = os.path.split(os.path.realpath(__file__))[0];
if length == 1:
    print("Convert Start!");
    ImageProcess("bmp_CArray.py", path);
elif length == 3:
    print("convert to c");
    print(sys.argv[1])
    inpath = path + "\\" + sys.argv[1];
    outpath = path + "\\" + sys.argv[2];
    FileHex(inpath, outpath);