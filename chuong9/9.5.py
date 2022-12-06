n=int(input('nhập n:'))
x=int(input('nhập x:'))
def tinh_a(n,x):
    A = (x**2 + x + 1)**n + (x**2 - x + 1)**n
    return A
print('A=',tinh_a(n,x))


