from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(start):
    print(start, end=' ')
    visited[start] = 1
    
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1

    while que:
        v = que.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 1

visited = [0] * (N+1)
dfs(V)
print()

visited = [0] * (N+1)
bfs(V)
