#xét kết quả học tập 
diem_tb = eval(input("nhập điểm trung bình: "))
if diem_tb >=0 and diem_tb <=10:
    if diem_tb < 5:
        print("yếu/kém!!")
    elif diem_tb <6:
        print("trung bình")
    elif diem_tb<7:
        print("trung bình - khá")
    elif diem_tb<8:
        print("khá")
    elif diem_tb<9:
        print("giỏi")
else:
    print("điểm nhập không hợp lệ, hayx nhập lại")        
