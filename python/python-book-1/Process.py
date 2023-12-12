
import random


class weapon:

    #定义基本属性
    level = 0
    name = ''
    resource = 0
    
    #定义私有属性
    __delres = 0

    def __init__(self, name, level, resource):
        self.name = name
        self.level = level
        self.resource = resource

    def ods(self, setotal, setobs):
        if(random.randint(0, setotal) in range(setobs)):
            return True
        return False

    def up(self):
        
        #满级情况下不处理
        if(self.level == 5):
            print("已经满级, 不要升级")
            return True

        #每次升级消耗的资源
        if(self.level+1 > 5 ):
            self.__delres = 5;
        else:
            self.__delres = self.level + 1
        
        if(self.resource < self.__delres):
            print("资源不足, 无法升级")
            return True
        else:
            self.resource -= self.__delres

        #计算升级概率
        if(self.level == 0):
            self.level += 1
        elif(self.level == 1):
            if(self.ods(100, 60)):
                self.level += 1
        elif(self.level in [2, 3]):
            if(self.ods(100, 20)):
                self.level += 1
            if(self.ods(100, 35)):
                self.level = 1
            else:
                pass
        else:
            if(self.ods(100, 5)):
                self.level += 1
            if(self.ods(100, 7)):
                self.level = 2
            if(self.ods(100, 3)):
                self.level = 1
            else:
                pass
                
        print("weapon level:", self.level, "", "currnet resource", self.resource)
        return False

wp = weapon("sword", 0, 1000)

for i in range(1000):
    if(wp.up()):
        break