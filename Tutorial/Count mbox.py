fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ("Can't find " + fname + " file")
    quit()
    
lst = list()
for line in fh:
    if not line.startswith("From "):
        continue
    line = line.split()
    lst.append(line[1])
    
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1
    print(counts)

bigcount = None
bigword = None
for cum,cunt in counts.items(): 
    if bigcount is None or cunt > bigcount:
        bigcount = cunt
        bigword = cum

print (bigword,bigcount)
    


