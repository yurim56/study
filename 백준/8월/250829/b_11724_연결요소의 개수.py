# N, M = map(int, input().split())

# graph = [[] for _ in range(N+1)]
# visited = [0] * (N+1)
# count = 0

# def dfs(node):
#     # print(node, end=' ')
#     visited[node] = 1

#     for i in graph[node]:
#         if visited[i] == 0:
#             dfs(i)

# for _ in range(M):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# for i in range(1, N+1):
#     if visited[i] == 0:
#         dfs(i)
#         count += 1

# # print(count)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 0

def dfs(node):
    visited[node] = 1

    for i in graph[node]:
        if visited[i] == 0:
            dfs(i)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for k in range(1, N+1):
    if visited[k] == 0:
        dfs(k)
        count += 1

print(count)