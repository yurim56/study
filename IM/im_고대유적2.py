dr = [0, 1] # 우, 하
dc = [1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N c M 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for r in range(N): # 행순회 하다가
        for c in range(M):
            if arr[r][c] == 1: # 1인 지점을 발견
                for i in range(2):
                    cnt = 1 # 현재 좌표부터 카운팅
                    nr, nc = r + dr[i], c + dc[i] # 우, 하
                    while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                        cnt += 1
                        nr += dr[i] # 좌표 이동
                        nc += dc[i]
                    if cnt >= 2: # 최소 길이가 2이상인 경우만 고려
                        max_cnt = max(max_cnt, cnt)

    print(f'#{tc} {max_cnt}')


T = int(input())

# 상하좌우 4방향 델타 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                # 4가지 방향으로 탐색 시작
                for i in range(4):
                    cnt = 1 # 현재 위치부터 카운트 시작
                    ny, nx = y + dy[i], x + dx[i]

                    # 같은 방향으로 연속된 1의 길이를 세기 위한 while 루프
                    while 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1:
                        cnt += 1
                        ny += dy[i]
                        nx += dx[i]

                    # ⚠️ 길이가 2 이상일 때만 최대 길이 갱신
                    if cnt > max_cnt and cnt >= 2:
                        max_cnt = cnt

    print(f'#{tc} {max_cnt}')