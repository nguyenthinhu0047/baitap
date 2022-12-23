lst = []
while True:
    a = int(input('nhập giá trị :'))
    hoi = input('(tiếp tục nhập giá trị?(1/0):')
    lst.insert(0,a)
    if hoi == '0':
        lst.reverse()
        print('list:',lst)
        break
x =int(input('nhập vào số x:'))
#tổng list
sum = 0
for num in lst:
    sum += num
print(sum)
y = lst.count(x)
print(x,'xuất hiện ',y,'lần trong list')
lst.find(5)