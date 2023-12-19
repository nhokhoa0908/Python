name = input("Enter file:")
if len(name) < 1 : name = "Trace.txt"
hf = open(name)

d=dict()

count = 0
count2 = 0

for line in hf:
    if not line.startswith("Name: "): 
        continue
    else:    
        line=line.split("-")
        line=line[1]
        d[line]=d.get(line,0)+1
        
lst=list()
for value,count in d.items():
    lst.append((value,count))
            
lst.sort()
for value,count in lst:
    print(value,count)

