dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

orders = input()

x, y = 0, 0 # 시작을 0,0에서 하니까
dir = 0 # 처음에 북쪽을 행한 상태에서

for order in orders:
    if order == 'L':
        dir = (dir+3)%4
    elif order == 'R':
        dir = (dir+1)%4
    else:
        x += dr[dir]
        y += dc[dir]

print(x, y)