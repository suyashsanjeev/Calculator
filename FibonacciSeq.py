def fib(n):
    if(n<=1):
        return n
    return(fib(n - 1) + fib(n - 2))
print('What number of fibonacci sequence?')
n = int(input())
print(fib(n))
