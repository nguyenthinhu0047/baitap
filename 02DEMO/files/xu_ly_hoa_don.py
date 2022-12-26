import os
__path=""






# quan ly hoa don
lstHoaDon =[]
  #Hàm 3 
def mo_file_hoa_don(lstHoaDon):
    return
def luu_danh_sach_hoa_don(lstHoaDon):
    return
def them_hoa_don(lstHoaDon):
 while True:
    so_hd=input('Nhập số hoá đơn: ')
    ngay_hd=input('Ngày hoá đơn')
    ho_tenkh=input('Họ tên khách hàng: ')
    dia_chi=input('Địa chỉ khách hàng: ')
    quan=input('Quận: ')
    dien_thoai=input('Điện thoại: ')
    tong_tien_hd=float(input('Tổng tiền hợp đồng: '))
    tam_ung=float(input("Tạm ứng: "))
    con_lai=float(tong_tien_hd-tam_ung)
    lstHoaDon.append({'so_hd':so_hd,'ngay_hd':ngay_hd,\
        'ho_tenkh':ho_tenkh,'dia_chi':dia_chi,'quan':quan,\
    'dien_thoai':dien_thoai,'tong_tien_hd':tong_tien_hd,\
            'tam_ung':tam_ung,'con_lai':con_lai})
#Hết lệnh append
    tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
    if tt!='1':
        break
 return
print(them_hoa_don(lstHoaDon))
print(lstHoaDon)
 
 #Hàm 4
def in_ds_hoa_don(lstHoaDon):
    print('{:12}{:12}{:28}{:18}{:20}{:15}{:20}{:20}{:20}'.format('so_hd','ngay_hd','ho_tenkh','dia_chi','quan','dien_thoai','tong_tien_hd',"tam_ung",'con_lai'))
    for hd in lstHoaDon:
     print('{:12}{:12}{:28}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(hd['so_hd'],hd['ngay_hd'],hd['ho_tenkh'],hd['dia_chi'],hd['quan'],hd['dien_thoai'],hd['tong_tien_hd'],\
        hd['tam_ung'],hd['con_lai']))
    return
in_ds_hoa_don(lstHoaDon)
def tra_cuu_hoa_don(lstHoaDon):
    return lstHoaDon
def thong_ke(lstHoaDon):
    return 
def xoa_hoa_don(lstHoaDon):
    return
def luu_danh_sach_phan_tu(lstHoaDon):
    return
def doc_hoa_don(lstHoaDon):
    return
def mo_file_hoa_don(lstHoaDon):
    return
#3   
print('CHƯƠNG TRÌNH QUẢN LÝ HOÁ ĐƠN')
while True:
    print('1:Thêm hoá đơn')
    print('2: Danh sách hoá đơn')
    print('3: Tra cứu hoá đơn')
    print('4: Xoá hoá đơn')
    print('5:Thống kê')
    print('6:Lưu danh sách hoá đơn ra file csv')

    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon==1:
        them_hoa_don(lstHoaDon)
    elif chon==2:
        in_ds_hoa_don(lstHoaDon)
    elif chon==3:
        tra_cuu_hoa_don(lstHoaDon)
    elif chon==4:
        xoa_hoa_don(lstHoaDon)
    elif chon==5:
        thong_ke(lstHoaDon)
    elif chon==6:
        luu_danh_sach_phan_tu(lstHoaDon) 
    else:
        print('Misson complete!!!')
        break 
