# 밑에서부터 올라올 것 -> 상, 좌, 우의 좌표만 필요
dr = [-1, 0, 0]
dc = [0, -1, 1]

final_dir = [[1,2,0],[0,1],[0,2]]

for tc in range(1, 11):
    input()
    labber = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    c = labber[99].index(2)
    dir = 0

    while r > 0:
        for i in range(len(final_dir[dir])):
            next_dir = final_dir[dir][i]
            nr = r + dr[next_dir]
            nc = c + dc[next_dir]

            if 0 <= nc <= 99 and labber[nr][nc] == 1:
                dir = next_dir
                r = nr
                c = nc
                break
    
    print(f'#{tc} {c}')