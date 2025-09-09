dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

def dfs(r, c):
    visited[r][c] = 1

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]

        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc)

for _ in range(T):
    M, N, K = map(int, input().split())
    
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    count = 0
    
    for _ in range(K):
        X, Y = map(int, input().split())
    
        graph[Y][X] = 1

    for row in range(N):
        for col in range(M):
            if graph[row][col] == 1 and visited[row][col] == 0:
                dfs(row, col)
                count += 1
    
    print(count)




# T = int(input())

# for tc in range(1, T + 1):
#     N, M = map(int, input().split()) 
#     graph = [list(map(int, input().split())) for _ in range(N)]

#     max_pang = 0 

#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, 1, -1]

#     for r in range(N):
#         for c in range(M):
#             current_pang = graph[r][c]
#             power = graph[r][c]

#             for i in range(4):
#                 for p in range(1, power + 1):
#                     nr = r + dr[i] * p
#                     nc = c + dc[i] * p

#                     if 0 <= nr < N and 0 <= nc < M:
#                         current_pang += graph[nr][nc]
            
#             if current_pang > max_pang:
#                 max_pang = current_pang

#     print(f"#{tc} {max_pang}")