import os
import sys
import six

from struct import *

#hex to bin
def hex_bin(hexfile,binfile):    
    fin = open(hexfile, 'r')
    fout = open(binfile,'wb')
    result = []
    print("start, Infile:", hexfile)
    for hexstr in fin.readlines():
        hexstr = hexstr.strip()
        print(hexstr)
        size = int(hexstr[1:3],16)
        if int(hexstr[7:9],16) != 0:
            continue     
        for h in range(0, size):
            b = int(hexstr[9+h*2:9+h*2+2],16)
            result.append(six.int2byte(b))
        fout.write(b''.join(result)) 
        result = []       
    print("end, Outfile:", binfile)
    fin.close()
    fout.close()

   
if len(sys.argv) != 3:
    print('usage:')
    print('convert hexadecimal format to binary format:')
    print('hexbin.py hexfile binfile')
    exit(0)
   
hex_bin(sys.argv[1],sys.argv[2])