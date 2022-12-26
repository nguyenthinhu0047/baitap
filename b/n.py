def tinh_tien_tro_cap(ho_ngheo,so_tv):
    if (ho_ngheo or so_tv >=5):
                return 1000000*so_tv
    elif (ho_ngheo,3 <= so_tv < 5):
                return 800000*so_tv  
    elif (ho_ngheo ,1<= so_tv <3):
                return 500000*so_tv           
print(tinh_tien_tro_cap(ho_ngheo,so_tv))