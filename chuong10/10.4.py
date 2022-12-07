import math
x=int(input())
n=int(input())
A=math.pow(math.pow(x,2)+x+1,n)
B=math.pow(math.pow(x,2)-x+1,n)
print(A+B)