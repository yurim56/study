def dfs(now):
    visited[now] = 1

    for next_node in graph[now]:
        if visited[next_node] == 0:
            dfs(next_node)

T = int(input())

for tc in range(1, T+1):
    
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V+1)]
    
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    visited = [0] * (V+1)
    
    dfs(S)

    if visited[G] == 1:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')