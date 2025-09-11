dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(row, col):
    visited[row][col] = 1
    
    for dir in range(4):
        nr = row + dr[dir]
        nc = col + dc[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        if graph[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc)


N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

count = 0

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and visited[r][c] == 0:
            dfs(r, c)
            count += 1

print(count)