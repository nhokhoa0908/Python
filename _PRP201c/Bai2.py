name = input("Enter file:")
if len(name) < 1 : name = "Text.txt"
hf = open(name)

for line in hf: 
        line=line.split(",")
        a=line[0]
        b=line[1]
        c=line[2]
        print(a)
        print(b)
        print(c)
        
        


