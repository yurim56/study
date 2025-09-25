from collections import deque
import sys
sys.setrecursionlimit(10000)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(r, c):
    que = deque([(r, c)])
    graph[r][c] = 0
    
    while que:
        a, b = que.popleft()
        
        for dir in range(4):
            nr = a + dr[dir]
            nc = b + dc[dir]
            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 1:
                que.append((nr, nc))
                graph[nr][nc] = 0

T = int(input())

for _ in range(T):
    count = 0
    
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 1:
                bfs(row, col)
                count += 1
    
    print(count)