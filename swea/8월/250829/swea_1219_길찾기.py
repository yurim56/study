T = 10

def dfs(node):
    global ans

    if node == 99:
        ans = 1
        return
    
    for next_node in adj_list[node]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)

for _ in range(1, T+1):
    tc, M = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]
    ans = 0
    visited = [0]*100

    for i in range(M):
        a = arr[2*i]
        b = arr[2*i+1]

        adj_list[a].append(b)

    visited[0] = 1
    dfs(0)
