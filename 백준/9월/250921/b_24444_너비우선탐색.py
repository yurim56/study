from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

visited = [0] * (N+1)
order_list = [0] * (N+1)
order = 1

que = deque([R])
visited[R] = 1
order_list[R] = order

while que:
    cur = que.popleft()
    for i in graph[cur]:
        if visited[i] == 0:
            visited[i] = 1
            que.append(i)
            order += 1
            order_list[i] = order

for i in range(1, N+1):
    print(order_list[i])