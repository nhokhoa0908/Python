flag = 0
while(flag==0):
    dnumber = input("Enter a day:")
    mnumber = input("Enter a month:")
    ynumber = input("Enter a year:")
    try:
        dnumber = int(dnumber)
        mnumber = int(mnumber)
        ynumber = int(ynumber)
        if ynumber%400!=0 and mnumber == 2 and dnumber >= 29:
            print ("Invalid day!")
            flag = 0
            continue
        if dnumber < 1  or mnumber < 1 or ynumber < 1:
            print ("Positive number only!")
            flag = 0
            continue
        if dnumber > 31  or mnumber > 12:
            print ("Wrong format!")
            flag = 0
            continue
        if mnumber == 4 and dnumber > 30:
            print ("Invalid day!")
            flag = 0
            continue
        if mnumber == 6 and dnumber > 30:
            print ("Invalid day!")
            flag = 0
            continue
        if mnumber == 9 and dnumber > 30:
            print ("Invalid day!")
            flag = 0
            continue
        if mnumber == 11 and dnumber > 30:
            print ("Invalid day!")
            flag = 0
            continue
        else:
            print ("Valid day!")
            flag=1
    except:
       print ("Wrong format!")
       flag = 0  