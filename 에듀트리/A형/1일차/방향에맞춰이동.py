dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
order = ['W', 'E', 'S', 'N']

N = int(input())
r = c = 0
for _ in range(N):
    direction, length = input().split()
    length = int(length)
    
    for dir in range(4):
        if direction == order[dir]:
            r += dr[dir] * length
            c += dc[dir] * length
            break

print(r, c)
