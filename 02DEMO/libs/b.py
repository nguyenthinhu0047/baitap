ho_dan=input('nhập tên hộ dân')
thanh_vien=int(input('nhập số lượng thành viên'))
def tinh_tien_tro_cap(thanh_vien):
    if thanh_vien >=5:
                return 1000000*thanh_vien
    elif 3 <= thanh_vien < 5:
                return 800000*thanh_vien        
    elif 1<= thanh_vien <3:
                return 500000*thanh_vien   
print(tinh_tien_tro_cap(thanh_vien))
    
    