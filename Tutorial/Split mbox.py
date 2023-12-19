fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ("Can't find " + fname + " file")
    quit()
    
count = 0
for line in fh:
    line = line.rstrip()
    if line == "":
        continue
        
    words = line.split()
    if words[0] !="From":
        continue
        
    print(words[1])
    count = count+1

print("There were", count, "lines in the file with From as the first word")
