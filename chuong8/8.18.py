n=int(input('nhập số nguyên:'))
tong=0
for i in range(1,n):
    if(n%i==0):
        tong += i
if(tong == n):
    print(n,"Là số hoàn hảo")
else:
    print(n,"Không phải là số hoàn hảo")