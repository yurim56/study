T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    r = 0
    c = 0
    dir = 0
    
    for number in range(1, N*N+1):
        # 범위를 벗어나지 않았을 경우 or 만난 숫자가 0일 경우
        snail[r][c] = number
        nr = r + dr[dir]
        nc = c + dc[dir]

        if (0 <= nr < N and 0<= nc < N) and snail[nr][nc] == 0:
            r = nr
            c = nc
        else:
            dir = (dir+1)%4 # 방향 바꾸기
            r += dr[dir]
            c += dc[dir]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()