#usr/bin/python
import os
import time
from audio_parser import GetAudioWriter, ReadInt

class FLV:
    def __init__(self, filepath, fileData):
        self.start = time.perf_counter()
        self.filepath = filepath
        self.Data = fileData

    #FLV文件解析
    #| FLV(3) | version(1) | Contains(1) | headLength(4) |
    #| FLVBody(...)
    def Parser(self):
        try:
            self.hasVideo = False
            self.hasAudio = False
            self.headLength = 0
            self.version = 0
            self.headPos = 0
            self.fileLength = len(self.Data)

            #Audio Writer
            self.AudioWriter = None
            AudioData = []
            AudioType = ""

            #版本号(Bytes[3])
            self.version = self.Data[3]

            #视频和音频存在信息(Bytes[4])
            contains = self.Data[4]
            self.hasVideo = ((contains>>0)&0x01) == 0x01
            self.hasAudio = ((contains>>2)&0x01) == 0x01

            #文件头长度字节5-9
            self.headLength = ReadInt(self.Data[5:9], 4)

            #位置指向Tag1首位(Tag0默认为0，size长度为4)
            self.headPos = self.headLength + 4

            print("Start ", "TagHead:{0}".format(self.headPos), "fileLength:{0}".format(self.fileLength))
            
            #Tag处理
            while self.headPos < self.fileLength:
                TagType, Timestamp, TagData = self.FlvTag_Parser()

                #Audio Tag
                if TagType == 0x08:
                    Data, AudioType = self.AudioTag_Parser(TagData, Timestamp)
                    AudioData.append(Data)
                #Video Tag
                elif TagType == 0x09:
                    continue

                #Script Tag
                elif TagType == 0x12:
                    continue

                #Invalid Tag
                else:
                    raise ValueError("FLVTag Type Error")

            #获得文件输出地址, 并写入
            OutPath = '.'.join(self.filepath.split(".")[:-1]) + '.' + AudioType
            foutAudio = open(OutPath, 'wb')
            foutAudio.write(b''.join(AudioData))
            foutAudio.close()

            self.end = time.perf_counter();
            print("endTime: {0}s".format(self.end - self.start), OutPath)
            
        except Exception as e:
            print(e)

    def AudioTag_Parser(self, AudioTag, Timestamp):
        if self.AudioWriter == None:
            self.AudioWriter = GetAudioWriter(AudioTag[0])
            return self.AudioWriter["audio"].Parser(AudioTag, Timestamp), self.AudioWriter["audio"].Type
        elif self.AudioWriter["format"] == "aac":
            return self.AudioWriter["audio"].Parser(AudioTag, Timestamp), self.AudioWriter["audio"].Type
        else:
            raise ValueError("Invalid Audio Tag")

    def FlvTag_Parser(self):

        #tag解析文件头
        #TagType(1[5]) | Datasize(3) | Timestamp(3) | TimestampExtended(1)
        #| StreamID(3) | TagData(DataSize) 
        TagType = self.Data[self.headPos]&0x1f
        DataSize = ReadInt(self.Data[self.headPos + 1:self.headPos +4], 3)
        Timestamp = ReadInt(self.Data[self.headPos+4:self.headPos+7], 3)
        TimestampExtended = ReadInt(self.Data[self.headPos+7], 1)

        #获得TagData数据
        TagData = self.Data[self.headPos + 11:self.headPos +11+DataSize]

        #右移DataSize+11+4数据,等待下次处理
        #FLVBody格式
        #TagValue(11+Datasize) | Tagsize(4)
        self.headPos += (11+DataSize+4)

        return TagType, (TimestampExtended<<24)+Timestamp, TagData

def CreatObj(path):
    
    Obj = {
            "format": None,
            "video" : None,
          }
    try:
        #打开文件, 以二进制读取信息, 然后关闭文件
        Reader = open(path, "rb")
        Data = Reader.read()
        Reader.close()
    except:
        print("Open {0} Failed".format(path))

    #判断是否是FLV文件, 在确定后续处理
    if Data[0:3] == b"FLV":
        Obj["format"] = "flv"
        Obj["video"] = FLV(path, Data)
        return Obj
    else:
        return Obj

