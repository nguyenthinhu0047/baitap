a = int(input('nhập số a: '))
b = int(input('nhập số b :'))
if a == 0:
    if b == 0:
        print('phương trình vô số nghiệm')
    else:
        print('phương trình vô nghiệm')    
else:
    x = -b/a
    print('phương trình có nghiệm x= ',x)        