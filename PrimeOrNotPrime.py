for i in range(0, 21):    
    isPrime = True
    if i<2:
        print(i, 'is not prime nor composite.')
    elif i == 2:
        isPrime = True  
    else:
        for a in range(2, i):
            if i%a == 0:
                isPrime = False                
                break
            else:
                continue
        if isPrime == True:
            print(i, 'is prime')
        else:
            print(i, 'is not prime')
        
