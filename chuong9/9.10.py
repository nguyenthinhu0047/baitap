def fib(n):
    if ( n==0 or n==1):
        return 0
    elif n>=2:
        return (fib(n-1)+fib(n-2)) 
x=int(input('nhap n:'))
print(fib(x))