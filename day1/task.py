def open_data(path='test.txt'):
    with open(path, 'r') as f:
        reader = f.read()
    return reader
data = open_data('input.txt')
c = 0
for s in data:
    if s == '(':
        c += 1
    elif s == ')':
        c -= 1
print(c)


