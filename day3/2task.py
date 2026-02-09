def open_data(path):
    with open(path, 'r') as f:
        reader = f.read()
    return reader

data = open_data('input.txt')
pos = {}
state_robo = (0,0)
state_santa = (0,0)
pos[state_robo] = 1
pos[state_santa] += 1

for i, s in enumerate(data):
    if i%2 == 0:
        state = state_santa
    else:
        state = state_robo
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
    
    if i%2 == 0:
        state_santa = new_state
    else:
        state_robo = new_state

print(pos)
print(len(pos))
