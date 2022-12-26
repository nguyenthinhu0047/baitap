# quan ly hoa don
import os
__path=""
lsthodan =[]

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
        hongheo=input('bạn là hộ nghèo hay không?(0 bạn là hộ nghèo:1 bạn không là hộ nghèo)')
        if hongheo==0:
            return True
        while True:
            lsthodan.append({'ma_ho':ma_ho,'ten_ho':ten_ho,\
            'so_tv':so_tv,'muc_thu_nhap':muc_thu_nhap,'hongheo':hongheo})
            tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
            if tt!='1':
                return 
            break         
print(them_ho_dan(lsthodan))
print(lsthodan)
def ds_ho_dan(lsthodan):
    print('{:12}{:12}{:12}{:12}'.format('ma_ho','ten_ho','so_tv','muc_thu_nhap','hongheo'))
    for hd in lsthodan:
     print('{:12}{:12}{:9}{:12}'.format(hd['ma_ho'],hd['ten_ho'],hd['so_tv'],hd['muc_thu_nhap'],hd['hongheo']))
    return
print(ds_ho_dan(lsthodan))

def tinh_tien_tro_cap(so_tv):
    
    if 3 >= so_tv >=5:
                return 1000000*so_tv
    elif ( 3 <= so_tv < 5):
                return 800000*so_tv  
    elif ( 1<= so_tv <3):
                return 500000*so_tv 
tinh_tien_tro_cap
