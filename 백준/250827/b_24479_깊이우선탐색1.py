import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

visited = [0]*(N+1)
count = 1

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(start):
    global count
    visited[start] = count

    count += 1

    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])