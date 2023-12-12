#/usr/bin/python
import os
 
#count the line of a single file
def CountLine(path):
        tempfile = open(path)
        res = 0
        for lines in tempfile:
                if len(lines.strip()) != 0:
                        res += 1
        return res
 
#count the total line of a folder, sub folder included
def TotalLine(path):
        total = 0
        for root, dirs, files in os.walk(path):
                for item in files:
                        ext = item.split('.')
                        ext = ext[-1]  #get the postfix of the file
                        if(ext in ["cpp", "c", "h", "java", "py", "php"]):
                                subpath = root + "/" + item
                                total += CountLine(subpath)
        return total

path = os.path.split(os.path.realpath(__file__))[0];
print("Input Path:", path)
print(TotalLine(path))