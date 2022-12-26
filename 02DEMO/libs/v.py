# quan ly hoa don
lsthodan =[]
  #Hàm 3 
def mo_file_ho_dan(lsthodan):
    return
def luu_danh_sach_ho_dan(lsthodan):
    return
def them_ho_dan(lsthodan):
     while True:
        ma_ho=input('Nhập mã hộ dân')
        ten_ho=input('tên hộ dân: ')
       
        
        so_tv=int(input('số thành vien: '))
        muc_thu_nhap=float(input("mức thu nhập: "))
        ho_ngheo=input('hộ là')
        lsthodan.append({'ma_ho':ma_ho,'ten_ho':ten_ho,\
            'so_tv':so_tv,'muc_thu_nhap':muc_thu_nhap,'ho_ngheo':ho_ngheo})
#Hết lệnh append
        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt!='1':
            break
        return
print(them_ho_dan(lsthodan))
print(lsthodan)
 
 #Hàm 4

print('CHƯƠNG TRÌNH QUẢN LÝ HOÁ ĐƠN')
while True:
    print('1:Thêm hộ dân')
    print('2: Danh sách danh sách hộ dân')
    print('3: Tra cứu hộ dân')
    print('4: Xoá hoá đơn')
    print('5:Thống kê')
    print('6:Lưu danh sách ho dan ra file csv')

    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon==1:
        them_ho_dan(lsthodan)
    elif chon==2:
        in_ds_ho_dan(lsthodan)
    elif chon==3:
        tra_cuu_hoa_don(lsthodan)
    elif chon==4:
        xoa_ho_dan(lsthodan)
    elif chon==5:
        thong_ke(lsthodann)
    elif chon==6:
        luu_danh_sach_ho-dan(lsthodan) 
    else:
        print('Misson complete!!!')
        break 

 