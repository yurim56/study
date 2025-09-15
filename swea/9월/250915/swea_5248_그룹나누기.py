from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    que = deque(arr)
    couple = []
    
    while que:
        a = que.popleft()
        b = que.popleft()
        couple.append((a,b))
    
    graph = [[] for _ in range(N+1)]
    for a, b in couple:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (N+1)
    groups = 0
    
    for start in range(1, N+1):
        if visited[start]:
            continue
        
        groups += 1
        dq = deque([start])
        visited[start] = 1
        
        while dq:
            cur = dq.popleft()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = 1
                    dq.append(nxt)

    print(f'#{tc} {groups}')
                