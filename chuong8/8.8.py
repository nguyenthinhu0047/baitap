loai_phong = int(input('cho biết loại phòng này là loại: '))
so_đem = float(input('số đêm ở trong resort: '))
tiên_phong = float(0)
if loai_phong == 1:
    if so_đem < 2:
        tien_cuoc = 1260000
    elif so_đem <=3:
        tien_cuoc = (1260000 * 25/100) * so_đem
    elif so_đem >= 4:
        tien_cuoc = (1260000 * 30/100) * so_đem
    tien_phong = tien_cuoc   
    print('tiênf phòng loại 1 của quý khachs là: %0.2f'%tien_phong ,'đồng')



if loai_phong == 2:
    if so_đem < 2:
        tien_cuoc= 1550000
    elif so_đem <=3:
        tien_cuoc = (1500000 * 25/100) * so_đem
    elif so_đem >= 4:
        tien_cuoc = (1550000 * 30/100) * so_đem
    tien_phong = tien_cuoc 
    print('tiênf phòng loại 2 của quý khachs là : %0.2f '%tien_phong ,'đồng')