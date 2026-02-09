def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read().splitlines()
    data = []
    for line in reader:
        w, h, l = line.split('x')
        data.append((int(w),int(h),int(l)))

    return data 

data = open_data('input.txt')

area = 0
for dims in data:
    w, h, l = dims
    area += l*w*h
    area += 2*min(w+l, w+h, h+l)
print(area)


