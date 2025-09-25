from collections import deque

dh = [1, -1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split()) 

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def bfs():
    que = deque()
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if graph[h][r][c] == 1:
                    que.append((h, r, c))
        
    while que:
        h, r, c = que.popleft()
        for dir in range(6):
            nh = h + dh[dir]
            nr = r + dr[dir]
            nc = c + dc[dir]
            
            if not (0 <= nh < H and 0 <= nr < N and 0 <= nc < M):
                continue
            
            if graph[nh][nr][nc] == 0:
                graph[nh][nr][nc] = graph[h][r][c] + 1
                que.append((nh, nr, nc))
            
bfs()

answer = 0
for height in range(H):
    for row in range(N):
        for col in range(M):
            if graph[height][row][col] == 0:
                print(-1)
                # exit()
        
            answer = max(answer, graph[height][row][col])

print(answer - 1)