import pydev

#pydev的接口
#open(path:str, method:int, permission:Int)

permission: int = 0777;
path_name: str = '/tmp/file_test'

fd = pydev.open(path_name, pydev.O_CREAT | pydev.O_WRONLY, permission)
if fd >= 0:
    pydev.write(fd, b"hello world!")
    pydev.close(fd)

buffer = bytearray(12)
fd = pydev.open(path_name, pydev.O_RDONLY)
if fd >= 0:
    size = pydev.read(fd, buffer, 16)
    print(buffer.decode('utf-8'))
    pydev.close(fd)


