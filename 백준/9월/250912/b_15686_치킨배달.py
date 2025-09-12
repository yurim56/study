from itertools import combinations

N, M = map(int, input().split())

graph = [[0]*N for _ in range(N)]

home_rcs = []
store_rcs = []
answer = float('inf')

for r in range(N):
    row = list(map(int, input().split()))
    
    for c in range(N):
        graph[r][c] = row[c]

        if graph[r][c] == 1:
            home_rcs.append((r, c))
            
        elif graph[r][c] == 2:
            store_rcs.append((r, c))
        
# 열의 수가 store 수
distance = [[0]*len(store_rcs) for _ in range(len(home_rcs))]

for home_idx in range(len(home_rcs)):
    for store_idx in range(len(store_rcs)):
        
        distance[home_idx][store_idx] = abs(home_rcs[home_idx][0] - store_rcs[store_idx][0]) + abs(home_rcs[home_idx][1] - store_rcs[store_idx][1])


for store_idx_set in combinations(range(len(store_rcs)), M):
    
    distance = 0
    for home_idx in range(len(home_rcs)):
        min_distance = 2(N*-1) # 가장 왼쪽 위 ~ 오른쪽 아래의 거리 (N-1)*(N-1)
        for store_idx in store_idx_set:
            min_distance = min(min_distance, distance[home_idx][store_idx])
        
        distance += min_distance
    
    answer = min(answer, distance)

print(answer)