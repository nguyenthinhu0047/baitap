def dientichtg(a, b, c):
    p = (a+b+c)/2
    s = p* (p-a)*(p-b)*(p-c)
    return s**0.5


print('diện tích tam giác:', dientichtg(8, 5, 6))
