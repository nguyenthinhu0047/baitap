n=int(input("Nhập số n="))
i=int(1)
day_so = ""
print("Nhập dãy số, bắt đầu = số 1:")
while i<n:
    i=int(input("i="))
    day_so+=str(i)
#sử dụng chuỗi kết quả để đảo ngược dãy số nhập ở trên
kq=""
for ch in day_so:
    kq=ch+kq
#in ra các số lẻ theo thứ tự đảo ngược của dãy số
for ch in kq:
    if int(ch)%2 !=0:
        print(ch, end="")