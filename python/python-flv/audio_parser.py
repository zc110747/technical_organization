#usr/bin/python

#acc音频接口
class AudioAAC:
    
    def __init__(self):
        self.Type = "aac"
        self._accProfile = 0
        self._Frequencies = 0
        self._channelConfig = 0

    #参考网址 http://blog.csdn.net/bsplover/article/details/7426476
    #ADTS头
    def GetAACHeader(self, TagSize):
        ulong = 0
        offset = 0
        OutBytes = b""

        #syncword 12
        ulong |= 0xFFF<<(64-offset-12)  
        offset += 12     

        #ID 1      
        ulong |= 0<<(64-offset-1)       
        offset += 1

        #layer 2
        ulong |= 0<<(64-offset-2)       #layer     2
        offset += 2

        #absent 1
        ulong |= 1<<(64-offset-1)       
        offset += 1

        #Profile 2
        ulong |= (self._accProfile&0x03)<<(64-offset-2)
        offset += 2

        #sampling_frequency_index 4
        ulong |= (self._Frequencies&0x0f)<<(64-offset-4)
        offset += 4

        #private_bit 1
        ulong |= 0<<(64-offset-1)
        offset += 1

        #channel_configuration 3
        ulong |= (self._channelConfig&0x7)<<(64-offset-3)
        offset += 3

        #original_copy, home, copyright_bit, copyright_start 1
        ulong |= 0<<(64-offset-4)
        offset += 4

        #frame_length 13
        ulong |= ((TagSize + 7)&0x1FFF)<<(64-offset-13)
        offset += 13

        #buffer_fullness 11
        ulong |= 0x7FF<<(64-offset-11)
        offset += 11

        #numbers_raw_block 2
        ulong |= 0<<(64-offset-2)

        ulong = ulong>>8

        #将int->bytes
        OutBytes += ulong.to_bytes(7, "big")

        return OutBytes


    def Parser(self, AACTag, TimeStamp):
        self._accHeader = b""
        OutBytes = b""

        TagLen = len(AACTag)
        if TagLen < 2:
            return

        #AAC sequence Header
        #参考网址 http://blog.csdn.net/bsplover/article/details/7426511
        #Profile(5) | rateIndex(4) | _channelConfig(4) | ?(3)
        if AACTag[1] == 0:
            if TagLen < 4:
                return
            AACConf = ReadInt(AACTag[2:4], 2)

            self._accProfile = ((AACConf>>11)&0x1f) - 1
            self._Frequencies = (AACConf>>7)&0xf
            self._channelConfig = (AACConf>>3)&0xf

            #print(self._accProfile, self._Frequencies, self._channelConfig);

            if self._accProfile > 4:
                self._accProfile = 1

            if self._accProfile > 3 or self._accProfile<0:
                raise ValueError("unsported AAC Profile!")
            if self._Frequencies > 12:
                raise ValueError("No supported frequencies")
            if self._channelConfig > 7:
                raise ValueError("Invalid channel config")
            return b""

        #AACTag raw
        elif AACTag[1] == 1:
            TagLen -= 2
            OutBytes = self.GetAACHeader(TagLen) + AACTag[2:]
            return OutBytes
        else:
            raise ValueError("AudioTag Data Error!")

#mp3音频接口
class AudioMP3:
    def __int__(self):
        self.Type  = "mp3"


def GetAudioWriter(AudioInfo):

    Writer ={
        "format":None,
        "audio":None,
    }

    #AudioType
    #SoundFormate(4) | Rate(2) | Size(1) | Type(1)
    SoundFormat = AudioInfo>>4
    Rate  = (AudioInfo>>2)&0x03
    Size = (AudioInfo>>1)&0x01
    Type = AudioInfo&0x01

    if SoundFormat == 2:
        #return AudioMP3()
        Writer["format"] = "mp3"
        Writer["audio"] = AudioMP3()
    elif SoundFormat == 10:
        Writer["format"] = "aac"
        Writer["audio"] = AudioAAC()
    else:
        Writer["format"] = "None"
    return Writer;

def ReadInt(Bytes, length):
        if length > 1:
            total = 0
            index = 0
            for byte in Bytes:
                total += byte*(1<<((length-1)*8-index))
                index += 8
            return total
        else:
            return Bytes
