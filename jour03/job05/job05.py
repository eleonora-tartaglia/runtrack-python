for num in range (2,1001):
    for i in range (2,num):
        if (num % i) == 0:
            break
    else:
        print(num, "est un nombre premier")
        


