# Use words.txt as the file name
from ast import Try
from asyncore import read


fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ("Can't find " + fname + " file")
    quit()
for something in fh:
    a=something.rstrip()
    print(a.upper())