dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(row, col, h):
    
    visited[row][col] = 1
    
    for dir in range(4):
        nr = row + dr[dir]
        nc = col + dc[dir]
        
        if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] > h and visited[nr][nc] == 0:
            dfs(nr, nc, h)     

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
safe = 0

# max_h = max(map(max, graph))
best = -9999999999999999999
for i in graph:
    for v in i:
        if v > best:
            best = v
            
# for 
#     for r in range(N):
#         for c in range(N):
#             if graph[r][c] <= 4:
#                 graph[r][c] = 0
#             elif visited[r][c] != 1:
#                 graph[r][c] = 1
#                 dfs(r, c)
#                 safe += 1