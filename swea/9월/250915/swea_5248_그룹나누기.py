# from collections import deque

# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
    
#     couple = []
#     for i in range(0, len(arr), 2):
#         couple.append((arr[i], arr[i+1]))
    
#     graph = [[] for _ in range(N+1)]
#     for a, b in couple:
#         graph[a].append(b)
#         graph[b].append(a)
    
#     visited = [0] * (N+1)
#     groups = 0
    
#     for start in range(1, N+1):
#         if visited[start]:
#             continue
        
#         groups += 1
#         dq = deque([start])
#         visited[start] = 1
        
#         while dq:
#             cur = dq.popleft()
#             for nxt in graph[cur]:
#                 if not visited[nxt]:
#                     visited[nxt] = 1
#                     dq.append(nxt)

#     print(f'#{tc} {groups}')
                
                
# from collections import deque
  
# def bfs(start, graph, visited):
#     que = deque([start])
#     visited[start] = 1
    
#     while que:
#         cur = que.popleft()
#         for next in graph[cur]:
#             if visited[next] == 0:
#                 visited[next] = 1
#                 que.append(next)
  
# T = int(input())
  
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     arr = list(map(int,input().split()))
#     graph = [[] for _ in range(N+1)]    
#     visited = [0]*(N+1)
#     group_cnt = 0
    
#     for i in range(0, len(arr), 2):
#         a, b = arr[i], arr[i+1]  
#         graph[a].append(b)
#         graph[b].append(a)
        
#     for node in range(1, N+1):
#         if visited[node] == 0:
#             group_cnt += 1
#             bfs(node, graph, visited)

#     print(f'#{tc} {group_cnt}')

# # 부모찾기
# def Find(n):
#     if parent[n] != 0:
#         parent[n] = Find(parent[n])
#         return parent[n]
#     return n
 
# def union(a, b):
#     a = Find(a)
#     b = Find(b)
#     if a == b:
#         return
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
 
# T = int(input())
# for test_case in range(1, T + 1):
#     # N: 출석 번호, M: 신청서 장수
#     N, M = map(int, input().split())
#     # 신청서 리스트
#     lst = list(map(int, input().split()))
#     # 부모 리스트(초기값)
#     parent = [0]*(N+1)
#     # 부모 찾기
#     for i in range(0, len(lst), 2):
#         union(lst[i], lst[i+1])

#     # parent[0]의 0은 사용하지 않음
#     rlt = parent.count(0) - 1
 
#     print(f'#{test_case} {rlt}')

# -------------------강사님 리뷰------------------
# 1. DFS (인접 리스트 사용 -> 인접 행렬보다 메모리&시간 차원에서 더 좋음)
def dfs(node):
    for next in adj_list[node]:
        if visited[node] == 1:
            continue
        visited[next] = 1
        dfs(next)
        
T = int(input())

for tc in range(1, T+1):
    answer = 0
    
    N, M = map(int, input().split())
    connections = list(map(int, input().split()))
    
    adj_list = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    
    # for i in range(0, 2*M, 2):
    for i in range(M):
        idx1 = i*2
        idx2 = i*2 + 1

        a = connections[idx1]
        b = connections[idx2]
        
        adj_list[a].append(b)
        adj_list[b].append(a)
        
        # adj_list[connections[idx1]].append(connections[idx2])
        # adj_list[connections[idx2]].append(connections[idx1])
        
    for node in range(1, N+1):
        if visited[node] == 1:
            continue
        
        answer += 1
        visited[node] = 1 # dfs에 진입하기 전에 방문처리 해주는 걸로 권장
        dfs(node)
    
    print(f'#{tc} {answer}')

# 2. Union Find
# 부모 찾기
# def find_set(x):
#     if x == parents[x]:
#         return x

#     # 경로 압축
#     parents[x] = find_set(parents[x]) # 자기 부모로 가줘야함
#     return parents[x]

# def union_set(x, y):
#     x_parent = find_set(x)
#     y_parent = find_set(y)
    
#     if x_parent < y_parent:
#         parents[y_parent] = x_parent
    
#     elif x_parent > y_parent:
#         parents[x_parent] = y_parent
        
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     connections = list(map(int, input().split))
    
#     # make set
#     parents = [i for i in range(N+1)]
    
#     for i in range(0, 2*M, 2):
#         union_set(connections[i], connections[i+1])
    
#     for node in range(1, N+1):
#         find_set(node)
    
#     print(f'#{tc} {len(set(parents[1:]))}')