# Hàm tìm số lớn nhất
def find_max(a, b, c):
    max = a
    if max < b: max = b
    if max < c: max = c
    return max
 
       

# Chương trình chính

a = float(input('nhập vào số thứ nhât:'))
 
b = float(input('Nhập vào số thứ hai: '))
 
c = float(input('Nhập vào số thứ ba: '))
 
 
print("Số lớn nhất trong ba số ", a, " ", b, " ", c, " là ", find_max(a,b,c))
def find_min(a,b,c):
    min = a
    if min >b:
        min = b
    if min >c:
        min=c
    return min 
print("số bé nhất trong ba số ",a, "",b, "",c," là ", find_min(a,b,c)) 

