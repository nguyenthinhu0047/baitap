ho_dan=input('nhập tên hộ dân')
thanh_vien=input('nhập số lượng thành viên')
def tinh_tien_tro_cap(ho_dan,thanh_vien):
    if (ho_dan == 'hộ nghèo') or(thanh_vien >=5):
        tien_tro_cap=1000000*thanh_vien
        return tien_tro_cap
print(tinh_tien_tro_cap(ho_dan,thanh_vien)) 