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
        ho_ngheo=input('hộ là')
        lsthodan.append({'ma_ho':ma_ho,'ten_ho':ten_ho,\
            'so_tv':so_tv,'muc_thu_nhap':muc_thu_nhap,'ho_ngheo':ho_ngheo})

        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt!='1':
            break
        return
print(them_ho_dan(lsthodan))
print(lsthodan)
def ds_ho_dan(lsthodan):
    print('{:12}{:12}{:18}{:18}'.format('ma_ho','ten_ho','so_tv','muc_thu_nhap'))
    for hd in lsthodan:
     print('{:12}{:12}{:18}{:18}'.format(hd['ma_ho'],hd['ten_ho'],hd['so_tv'],hd['muc_thu_nhap']))
    return
print(ds_ho_dan(lsthodan))
def tinh_tien_tro_cap(ho_ngheo,so_tv):
    if (ho_ngheo and so_tv >=5):
                return 1000000*so_tv
    elif (ho_ngheo and 3 <= so_tv < 5):
                return 800000*so_tv  
    elif (ho_ngheo and 1<= so_tv <3):
                return 500000*so_tv          

def sap_xep_hd(lsthodan):
    lsthodan.sort()
    lsthodan.reverse()
print(lsthodan)