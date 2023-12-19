flag = 0
while(flag==0):
    fnumber = input("Enter a number:")
    try:
        fnumber = int(fnumber)
        if fnumber < 1:
            print ("Positive number only!")
            flag = 0
        else:
            print("The prime number from 0 to",fnumber)
            print([i for i in range(2, fnumber+1) if 0 not in [i%n for n in range(2, i)]])
            flag = 1
    except:
       print ("Wrong format!")
       flag = 0  