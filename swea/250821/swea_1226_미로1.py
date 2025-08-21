# T = 10

# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# def bfs(r, c):
#     visited = [[0]*16 for _ in range(16)]
#     que = [[r,c]]
#     visited[r][c] = 1

#     while que:
#         start_r, start_c = que.pop(0)
#         if graph[start_r][start_c] == 3:
#             return 1

#         for dir in range(4):
#             nr, nc = start_r + dr[dir], start_c + dc[dir]
#             if 0 <= nr < 16 and 0 <= nc < 16 and graph[nr][nc] != 1 and visited[nr][nc] == 0:
#                 que.append([nr,nc])
#                 visited[nr][nc] =  1
#     return 0
        

# for _ in range(1, T+1):
#     tc = int(input())
#     graph = [list(map(int,input())) for _ in range(16)]

#     for r in range(16):
#         for c in range(16):
#             if graph[r][c] == 2:
#                 st_r, st_c = r, c
#                 break
    
#     answer = bfs(st_r, st_c)
#     print(f'#{tc} {answer}')


from collections import deque

T = 10

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(r, c):
    visited = [[0]*16 for _ in range(16)]
    que = deque([[r,c]])
    visited[r][c] = 1

    while que:
        start_r, start_c = que.popleft()

        if graph[start_r][start_c] == 3:
            return 1
        
        for dir in range(4):
            nr, nc = start_r + dr[dir], start_c + dc[dir]
            if 0 <= nr < 16 and 0 <= nc < 16 and graph[nr][nc] != 1 and visited[nr][nc] == 0:
                que.append([nr, nc])
                visited[nr][nc] = 1
    
    return 0


for _ in range(1, T+1):
    tc = int(input())
    graph = [list(map(int,input())) for _ in range(16)]

    st_r, st_c = 0, 0
    for r in range(16):
        for c in range(16):
            if graph[r][c] == 2:
                st_r, st_c = r, c
                break
    
    answer = bfs(st_r, st_c)
    print(f'#{tc} {answer}')