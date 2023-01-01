def chuyen_doi(x):
    cd=x*0.0025
    return cd
list3=[74,74,72,72,69,69,71,76,71]
list_cd=list(map(chuyen_doi,list3))
print("List sau khi đổi từ inch sang mét:",list_cd)
print("3 chiều cao đầu tiên là:",list_cd[0:3])
print("3 chiều cao đầu tiên là:",list_cd[6:9])
tb=sum(list_cd)/len(list_cd)
print('chiều cao trung bình là: ',tb)
print('chiều cao lớn nhất là: ',max(list_cd))
print('chiều cao nhỏ nhất là: ',min(list_cd))
list_cd.sort()
print("chiều cao sắp xếp tăng dần là :",list_cd)
list_cd.sort()
list_cd.reverse()
print('chiều cao sắp xếp giảm dần là: ',list_cd)