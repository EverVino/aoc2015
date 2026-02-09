def open_data(path):
    with open(path, 'r') as f:
        reader = f.read()
    return reader

data = open_data('input.txt')
pos = {}
state = (0,0)
pos[state] = 1
for s in data:
    x,y = state
    if s == '^':
        ny = y +1
        nx = x
    if s == '>':
        ny = y
        nx = x + 1
    if s == '<':
        ny = y 
        nx = x - 1
    if s == 'v':
        ny = y - 1
        nx = x
    new_state = (nx,ny)
    if new_state not in pos:
        pos[new_state] = 1
    pos[new_state] += 1
    state = new_state
print(pos)
print(len(pos))
