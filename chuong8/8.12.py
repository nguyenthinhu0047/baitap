#kiểm tra 1 só có phải số nguyên tố không
import math
n = int(input('nhập 1 số n:'))

if n < 0:
    print('nhập số tự nhiee :')
elif n< 2:
    print('n không là số nguyên tố'.fomat(n))
else:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            print('n  không là số nguyên tố',n)
            break
    else:
        print('n là số nguyên tố',n)    

