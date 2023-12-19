import re

#file name is regex_sum_24962.txt
fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "regex_sum_24962.txt"
    
try:
    fh = open(fname)
except:
    print ("Can't find " + fname + " file")
    quit()
    
x=list()
for line in fh:
    y = re.findall('[0-9]+',line)
    x = x+y
    
sum=0
for z in x:
    sum = sum + int(z)

print(sum)