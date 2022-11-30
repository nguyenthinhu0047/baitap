
import math
print('nhập số đo các cạnh tam giácL:')
a=eval(input('a = '))
b=eval(input('b = '))
c=eval(input('c = '))
p=(a + b + c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('diện tích tam giác là :',s)