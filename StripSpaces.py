#File to strip repeated spaces and replace with a delimiter
import os
import string
import re
ifile = open("C:/Users/azaleski002/Desktop/c.txt","r")
ofile = open("C:/Users/azaleski002/Desktop/o.txt","w")
for line in ifile:
    nline = re.sub('  +', '|', line)
    ofile.write(nline)
    print(nline, end='')
ofile.close()