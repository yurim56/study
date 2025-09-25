from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

M, N= map(int, input().split()) 

graph = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    que = deque()
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 1:
                que.append((r,c))
    
    while que:
        r, c = que.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            
            if graph[nr][nc] == 0:
                graph[nr][nc] = graph[r][c] + 1
                que.append((nr, nc))
            
bfs()

answer = 0
for row in range(N):
    for col in range(M):
        if graph[row][col] == 0:
            print(-1)
            # exit()
        
        answer = max(answer, graph[row][col])

print(answer - 1)