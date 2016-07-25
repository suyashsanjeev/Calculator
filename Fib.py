n = 1
while n <= 10:    
    def fib(n):
        if(n<=1):
            return n
        return(fib(n - 1) + fib(n - 2))
    print(fib(n))
    if n > 10:
        break
    
