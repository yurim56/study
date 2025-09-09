dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    global count
    visited[r][c] = 1

    for dir in range(4):
        nr, nc = r + dr[dir], c + dc[dir]
        if 

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    count = 0

    graph = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for r in range(M):
        for c in range(N):
            if graph[r][c] == 1 and visited[r][c] == 0:
                dfs((r, c))
