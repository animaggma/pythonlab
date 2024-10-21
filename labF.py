num = int(input("Enter a number: "))


Isprime = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    
    for i in range(2, num):
        if (num % i) == 0:
             
            Isprime = True
            
            break

    
    if Isprime:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
