from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def bfs(r, c):
    que = deque([(r, c)])
    visited[r][c] = 1

    while que:
        cur_r, cur_c = que.popleft()

        for dir in range(4):
            nr = cur_r + dr[dir]
            nc = cur_c + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 1 and visited[nr][nc] == 0 :
                que.append((nr, nc))
                visited[nr][nc] = visited[cur_r][cur_c] + 1

bfs(0,0)

print(visited[N-1][M-1])