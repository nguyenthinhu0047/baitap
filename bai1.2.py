x = float(input('nhập số kwh tiêu thụ: '))
if x <= 50:
    y = x*1.678
if 51 <= x <= 100:
    y = 50*1.678 + (x-50)*1.734
if 101 <= x <= 200:
    y = 50*1.678 + 50*1.734 + (x-100)*2.014
if 201 <= x <= 300:
    y = 50*1.678 + 50*1.734 + 100*2.014 + (x-200)*2.534
if 301 <= x <= 400:
    y = 50*1.678 + 50*1.734 + 100*2.014 + 100*2.534 + (x-300)*2.834
if x >= 401:
     y = 50*1.678 + 50*1.734 + 100*2.014 + 100*2.534 + 100*2.834 + (x-400)*2.927         


print('số tiền điện phải trả là: ' ,y,'đồng')