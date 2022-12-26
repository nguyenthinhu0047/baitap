# quan ly hoa don
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
     print('{:12}{:12}{:18}{:18}'.format(hd['ma_ho'],hd['ten_hd'],hd['so_tv'],hd['muc_thu_nhap']))
    return
print(ds_ho_dan(lsthodan))
def tinh_tien_tro_cap(so_tv):
    if so_tv >=5:
                return 1000000*so_tv
    elif 3 <= so_tv < 5:
                return 800000*so_tv  
    elif 1<= so_tv <3:
                return 500000*so_tv           
