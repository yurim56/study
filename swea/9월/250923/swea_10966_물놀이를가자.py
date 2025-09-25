from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    global answer
    que = deque()

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W':
                # visited[r][c] = 0
                # 여기 append는 시작점 등록
                que.append((r, c))
    
    while que:
        r, c = que.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] =='L':
                visited[nr][nc] = visited[r][c] + 1
                # 여기는 새로운 칸 탐색할 때 등록
                que.append((nr, nc))
                answer += visited[nr][nc]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    answer = 0

    bfs()
    print(f'#{tc} {answer}')
    # print(visited)
    # total = 0
    # for row in visited:
    #     total += sum(row)
    # print(f'#{tc} {total}')