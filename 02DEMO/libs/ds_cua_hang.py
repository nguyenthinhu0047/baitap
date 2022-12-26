#ham tra cuu danh sach hoa don
def tra_cuu_hoa_don(lstHoaDon,sohd):
    for hd in lstHoaDon:
         if hd['so_hd'] ==sohd:
            return hd
    return
#-----ham xóa hóa đơn
def xoa_hoa_don(lstHoaDon, sohd):
    for i in range(len(lstHoaDon)):
        hd=lstHoaDon[i]
        if hd['so_hd']==sohd:
            del(lstHoaDon[1])
            return 1
    return 0
#------ham thống kê (thong_ke()),cho phép thống kê tiền hd
def thong_ke(lstHoaDon):
    tong=0
    tong_tamung=0
    