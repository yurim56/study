from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(row, col):
    global answer
    visited[row][col] = 1
    que = deque([(row, col)])
    
    while que:
        a, b = que.popleft()
        
        for dir in range(4):
            nr = a + dr[dir]
            nc = b + dc[dir]
            
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == 1 and visited[nr][nc] == 0:
                que.append((nr, nc))
                visited[nr][nc] = 1
                answer += 1   
    house.append(answer)
    answer = 1
    
N = int(input())

graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cluster = 0
house = []
answer = 1

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and visited[r][c] == 0:
            bfs(r, c)
            cluster += 1

print(cluster)
house.sort()
for i in house:
    print(i)