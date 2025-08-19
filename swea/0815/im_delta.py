T = int(input())

# 상하좌우 4방향 델타 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                for i in range(4):
                    count = 1
                    nr, nc = r + dr[i], c + dc[i]

                    while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                        count += 1
                        nr += dr[i]
                        nc += dc[i]

                    if count > max_cnt and count >= 2:
                        max_cnt = count
                  