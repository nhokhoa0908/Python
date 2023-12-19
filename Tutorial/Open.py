from asyncore import read


name = input("Enter file name:")
f=open(name,"rt")
print(f.read())