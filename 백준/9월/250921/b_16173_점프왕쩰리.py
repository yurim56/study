from collections import deque

dr = [1, 0]
dc = [0, 1]

def bfs(r, c):
    que = deque()
    que.append([r,c])

    while que:
        r, c = que.popleft()
        step = graph[r][c]
        visited[r][c] = 1

        if graph[r][c] == -1:
            print('HaruHaru')
            return
        
        for dir in range(2):
            nr = r + dr[dir] * step
            nc = c + dc[dir] * step

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue    
        
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1

                que.append([nr, nc])
        
    print('Hing')

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

bfs(0,0)