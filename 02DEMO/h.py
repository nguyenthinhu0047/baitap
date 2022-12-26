import os

__path=""
lsthodan =[]

def mo_file_ho_dan(lsthodan):
    return
def luu_danh_sach_ho_dan(lsthodan):
    return
def them_ho_dan(lsthodan):
    while True:
        ma_ho=input('Nhập mã hộ dân: ')
        ten_ho=input('tên hộ dân: ')
        
        so_tv=int(input('số thành vien: '))
        muc_thu_nhap=float(input("mức thu nhập: "))
        hongheo=input("Nhập hộ: ")
        if hongheo=='hộ nghèo':  
            print(bool(True))
        else:   
            print(bool(False))
        lsthodan.append({'ma_ho':ma_ho,'ten_ho':ten_ho,\
        'so_tv':so_tv,'muc_thu_nhap':muc_thu_nhap,'hongheo':hongheo})
        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt!='1':
            
            break
    return 
print(them_ho_dan(lsthodan))
def ds_ho_dan(lsthodan):
    print('{:12}{:12}{:18}{:18}'.format('ma_ho','ten_ho','so_tv','muc_thu_nhap','hongheo'))
    for hd in lsthodan:
     print('{:12}{:12}{:18}{:18}'.format(hd['ma_ho'],hd['ten_ho'],hd['so_tv'],hd['muc_thu_nhap'],hd['hongheo']))
    return
print(ds_ho_dan(lsthodan))
def Bool(hongheo):
    i
