#ví dụ hàm tính giai thừa đệ quy
def giaithua(n):
    if n == 1:
        return 1
    else:
        return (n* giaithua(n-1))    
number1 = 5
number2 = int(input('nhập số cần tính giai thừa:'))        
print("giai thừa của", number1, 'là',giaithua(number1))
print("giai thừa của", number2, 'là',giaithua(number2))
