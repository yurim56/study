# swea 1210
for tc in range(1, 2):
    T = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    idx = []
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                idx.append(i)
                idx.append(j)
    
    #ladder[99].index(2)

    dir = 0
    r = idx[0]  # 99
    c = idx[1]  # 57 

    while 0 < r:
        # 오른쪽
        if c < 99 and ladder[r][c+1] ==1:
            while c < 99 and ladder[r][c+1] ==1:
                c += 1
            r -= 1
        # 왼쪽
        elif c > 0 and ladder[r][c-1] ==1:
            while c >0 and ladder[r][c-1] ==1:
                c -= 1
            r -= 1
        # 위로
        else:
            r -= 1
    print(f'#{tc} {c}')