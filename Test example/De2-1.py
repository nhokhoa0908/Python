while True:
    number = input("Enter a positive integer number:")
    try:
        usVal = int (number)
        if usVal < 0:
            print("The number must be positive!")
            continue
        break
    except ValueError:
        print("Wrong format!")
        
for checkVal in range (1, usVal+1):
    total = 0
    for i in range(1, checkVal):
        if(checkVal % i == 0):
            total = total + i
            
    if(total == checkVal):
        print(checkVal, end="")
        