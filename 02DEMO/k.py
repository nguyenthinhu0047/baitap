# quan ly hoa don
import os,csv


__path=""
lsthodan =[]
def mo_file_ho_dan(_path,lsthodan):
    try:
        f=open(_path,'r', encoding ='utf-8')
        for hd in csv.reader(f):
            if hd[0]=='so_hd':
                continue
            lsthodan.append({'so_hd':hd[0],'ngay_hd':hd[1], 'ho_tenkh':hd[2],'dia_chi':hd[3],'quan':hd[4],\
            'dien_thoai':hd[5],'tong_tien_hd':hd[6],'tam_ung':hd[7],'con_lai':hd[8]})
        f.close()
        return 1
    except Exception as ex1:
        print('Khong mở được file hop le ', ex1)
    return
def luu_danh_sach_ho_dan(_path,lsthodan):
    try:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(['ma_ho','ten_chu_ho','so_thanh_vien','muc_thu_nhap'])
        for hd in lsthodan:
            csv.writer(f).writerow([hd['ma_ho'],hd['ten_chu_ho'], hd['so_thanh_vien'],hd['muc_thu_nhap']])
        f.close()
        return 1
    except Exception as ex1:
        return 0
def them_ho_dan(lsthodan):
     while True:
        ma_ho=input('Nhập mã hộ dân')
        ten_ho=input('tên hộ dân: ')
       
        so_tv=int(input('số thành vien: '))
        muc_thu_nhap=float(input("mức thu nhập: "))
        hongheo=input('bạn là hộ nghèo hay không?:,nếu không phải nhập là 0.')
        if hongheo=='hộ nghèo':
            print(bool(hongheo))
        else:
            print(bool(hongheo))
        lsthodan.append({'ma_ho':ma_ho,'ten_ho':ten_ho,\
            'so_tv':so_tv,'muc_thu_nhap':muc_thu_nhap,'hongheo':hongheo})

        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt!='1':
            break
        return
print(them_ho_dan(lsthodan))
print(lsthodan)
def ds_ho_dan(lsthodan):
    print('{:12}{:12}{:18}{:18}'.format('ma_ho','ten_ho','so_tv','muc_thu_nhap','hongheo'))
    for hd in lsthodan:
     print('{:12}{:12}{:18}{:18}'.format(hd['ma_ho'],hd['ten_ho'],hd['so_tv'],hd['muc_thu_nhap'],hd['hongheo']))
    return
print(ds_ho_dan(lsthodan))
def tra_cuu_ho_dan(lsthodan):
    for hd in lsthodan:
        if hd['ma_ho']==hd:
            return hd
    return
def xoa_ho_dan(lsthodan):
    for i in range(len(lsthodan)):
        hd=lsthodan[i]
        if hd['so_hd']==ma_ho:
            del(lsthodan[i])
            return 1
    return 0
def tinh_tien_tro_cap(thanh_vien):
    if (thanh_vien) >= 5:
                return 1000000*thanh_vien
    elif 3 <= (thanh_vien) < 5:
                return 800000*thanh_vien        
    elif 1<= (thanh_vien) <3:
                return 500000*thanh_vien   
    return tinh_tien_tro_cap(lsthodan)
print('CHƯƠNG TRÌNH QUẢN LÝ HOÁ ĐƠN')
while True:
    print('1:Thêm hoá đơn')
    print('2: Danh sách hoá đơn')
    print('3: Tra cứu hoá đơn')
    print('4: Xoá hoá đơn')
    print('5:Lưu danh sách hoá đơn ra file csv')
    print('6:tính tiền trợ cấp')
    print('7: mở file csv ')

    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon==1:
        them_ho_dan(lsthodan)
    elif chon==2:
        ds_ho_dan(lsthodan)
    elif chon==3:
        tra_cuu_ho_dan(lsthodan)
    elif chon==4:
        xoa_ho_dan(lsthodan)
    elif chon==5:
        luu_danh_sach_ho_dan(lsthodan)
    elif chon==6:
        tinh_tien_tro_cap(lsthodan)
    elif chon==7:
     if mo_file_ho_dan(__path,lsthodan):
            print("Đã đọc được file vào lsthodan ")
    else:
        print('Misson complete!!!')
        break
