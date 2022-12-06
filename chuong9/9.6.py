
x=int(input("Nhập số nguyên tố:"))
def kiem_tra_so_nguyen_to(x):
     if x%1==0 and x%x == 0:
        print("True",x)
     if x%2==0:
        print("Flase",x)