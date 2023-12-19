
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print ("Can't find " + fname + " file")
    quit()
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    t=line.find("0")
    number= float(line[t:])
    count = count + 1
    total = total + number

average = total/count
print("Average spam confidence: " ,average)