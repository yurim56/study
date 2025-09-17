from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

c = 1






# c = 1
# def bfs(node):
#     global c
#     visited[node] = 1
#     que = deque()
#     que.append(node)
    
#     while que:
#         a = que.popleft()
#         order.append(a)
        
#         for next in adj[a]:
#             if visited[next] == 1:
#                 continue
#             visited[next] = 1
#             que.append(next)

#     return order    
    
# N, M, R = map(int, input().split())

# adj = [[] for _ in range(N+1)]
# visited = [0] * (N+1)

# for _ in range(M):
#     u, v = map(int, input().split())
    
#     adj[u].append(v)
#     adj[v].append(u)

# for i in range(1, N+1):
#     adj[i].sort()

# print(*bfs(R))