#/usr/bin/python
import os
import binascii
import shutil 
from functools import partial
import re
import gzip

#创建一个新文件夹
def mkdir(path):
    path=path.strip()
    isExists=os.path.exists(path)
 
    #判断文件夹是否存在，不存在则创建
    if not isExists:
        os.makedirs(path)
        print(path+' 创建成功')
    else:
        pass
    return path

#删除一个文件夹(包含内部所有文件)
def deldir(path):
    path = path.strip()

    isExists=os.path.exists(path)
 
    #判断文件夹是否存在，不存在则创建
    if isExists:
        shutil.rmtree(path)
        print(path + "删除成功")
    else:
        pass

#网页一次压缩文件
def FileReduce(inpath, outpath):
        infp = open(inpath, "r", encoding="utf-8")
        outfp = open(outpath, "w", encoding="utf-8")
        for li in infp.readlines():
            if li.split():
                #去除多余的\r \n
                li = li.replace('\n', '').replace('\t', '');
                #空格只保留一个
                li = ' '.join(li.split())
                outfp.writelines(li)
        infp.close()
        outfp.close()
        print(outpath+" 压缩成功")

#shell命令行调用(用ugllifyjs来压缩js文件)
def ShellReduce(inpath, outpath):
    Command = "uglifyjs "+inpath+" -m -o "+outpath
    print(Command)
    os.system(Command)

#gzip压缩模块
def FileGzip(inpath, outpath):
    with open(inpath, 'rb') as plain_file:
        with gzip.open(outpath, 'wb') as zip_file:
            zip_file.writelines(plain_file)
    print(outpath+" gzip-压缩成功")

#将文件以二进制读取, 并转化成数组保存
def FileHex(inpath, outpath):
    i = 0
    count = 0
    a = ''
    inf = open(inpath, 'rb');
    outf = open(outpath, 'w')
    records = iter(partial(inf.read, 1), b'')
    for r in records:
        r_int = int.from_bytes(r, byteorder='big')  
        a +=  hex(r_int) + ', '
        i += 1
        count += 1
        if i == 16:             
            a += '\n'
            i = 0
    a = "const static char " + outpath.split('.')[-2].split('/')[-1] + "["+ str(count) +"]={\n" + a + "\n};\n\n" 
    outf.write(a)
    inf.close()
    outf.close()
    print(outpath + " 转换成数组成功")

def unCommentReduce(inpath, outpath):
    infp = open(inpath, "r", encoding="utf-8")
    outfp = open(outpath, "w", encoding="utf-8")
    fileByte = infp.read();

    replace_reg = re.compile('/\*[\s\S]*?\*/')
    fileByte = replace_reg.sub('', fileByte)
    fileByte = fileByte.replace('\n', '').replace('\t', '');
    fileByte = ' '.join(fileByte.split())
    outfp.write(fileByte)
    infp.close()
    outfp.close()
    print(outpath+"去注释 压缩成功!")

#程序处理主函数
def WebProcess(path):
        #原网页 ..\basic\  
        #压缩网页 ..\reduce\
        #gzip二次压缩 ..\gzip
        #编译完成.c网页 ..\programe
        BasicPath = path + "\\basic"
        ReducePath = path + "\\reduce"
        GzipPath = path + "\\gzip"
        ProgramPath = path + "\\program"
        #删除原文件夹，再创建新文件夹
        deldir(ProgramPath)
        deldir(ReducePath)
        deldir(GzipPath)
        mkdir(ProgramPath)

        for root, dirs, files in os.walk(BasicPath):
                for item in files:
                        ext = item.split('.')
                        InFilePath = root + "/" + item
                        OutReducePath = mkdir(root.replace("basic", "reduce")) + "/" + item
                        OutGzipPath = mkdir(root.replace("basic", "gzip"))  + "/" + item + '.gz'
                        OutProgramPath = ProgramPath + "/" + item.replace('.', '_') + '.c'

                        #根据后缀不同进行相应处理
                        #html 去除'\n','\t', 空格字符保留1个
                        #css  去除\*......*\注释数据、'\n'和'\t', 同时空格字符保留1个
                        #js 调用uglifyjs2进行压缩
                        #gif jpg ico 直接拷贝 
                        #其它 直接拷贝
                        #上述执行完毕后压缩成.gz文件
                        #除其它外，剩余文件同时转化成16进制数组, 保存为.c文件
                        if ext[-1] == 'html':
                            FileReduce(InFilePath, OutReducePath)
                            FileHex(OutReducePath, OutProgramPath)
                            FileGzip(OutReducePath, OutGzipPath)
                        elif ext[-1] == 'css':
                            unCommentReduce(InFilePath, OutReducePath)
                            FileHex(OutReducePath, OutProgramPath)
                            FileGzip(OutReducePath, OutGzipPath)
                        elif ext[-1] == 'js':
                            ShellReduce(InFilePath, OutReducePath)
                            FileHex(OutReducePath, OutProgramPath)
                            FileGzip(OutReducePath, OutGzipPath)
                        elif ext[-1] in ["gif", "jpg", "ico"]:
                            shutil.copy(InFilePath, OutReducePath)
                            FileHex(OutReducePath, OutProgramPath)
                            FileGzip(OutReducePath, OutGzipPath)
                        else:
                            shutil.copy(InFilePath, OutReducePath)


#获得当前路径
path = os.path.split(os.path.realpath(__file__))[0];
WebProcess(path)