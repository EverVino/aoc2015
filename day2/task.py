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
    area += 2*w*h + 2*h*l + 2*w*l
    area += min(w*h, w*l, h*l)
print(area)


