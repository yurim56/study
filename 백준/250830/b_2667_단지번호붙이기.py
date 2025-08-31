# from collections import deque

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# N = int(input())

# graph = [list(map(int, input())) for _ in range(N)]
# visited = [[0]*N for _ in range(N)]

# complex_sizes = []

# def bfs(r,c):
#     que = deque([(r,c)])
#     visited[r][c] = 1
#     size = 1 # 시작점

#     while que:
#         row, col = que.popleft()

#         for dir in range(4):
#             nr = row + dr[dir]
#             nc = col + dc[dir]

#             if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == 1 and visited[nr][nc] == 0:
#                 que.append((nr, nc))
#                 visited[nr][nc] = 1
#                 size += 1
        
#     return size
    
# for r in range(N):
#     for c in range(N):
#         if graph[r][c] == 1 and visited[r][c] == 0:
#             size = bfs(r, c)
#             complex_sizes.append(size)

# print(len(complex_sizes))
# complex_sizes.sort()
# for size in complex_sizes:
#     print(size)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N = int(input())

graph = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
complex_sizes = []

def dfs(r, c):
    visited[r][c] = 1
    size = 1

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]

        if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == 1 and visited[nr][nc] == 0:
            size += dfs(nr, nc)
    
    return size

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and visited[r][c] == 0:
            size = dfs(r, c)
            complex_sizes.append(size)

print(len(complex_sizes))
complex_sizes.sort()
for size in complex_sizes:
    print(size)