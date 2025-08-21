'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''

def bfs(s, V):
    # 초기화
    visited = [0] * (V+1) # visited 생성
    q = [s] # 큐 생성
            # 시작점 인큐 -> 한 번에 설정 가능
    visited[s] = 1 # 시작점 인큐 표시
    # 반복
    while q: # 탐색할 정점이 남아 있으면
        t = q.pop(0) # 디큐
        print(t) # visited(), 방문 정점 출력
        for w in adj_lst[t]: # 인접하고 미방문인 정점 인큐, 인큐 표시
            if visited[w] == 0: # 아직 간 적이 없는 곳
                q.append(w)
                visited[w] = visited[t] + 1

V, E = map(int, input().split()) # 마지막 정점, 간선 수

arr = list(map(int, input().split()))

# 인접리스트
adj_lst = [[] for _ in range(V+1)] # V번행까지 준비
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_lst[v1].append(v2)
    adj_lst[v2].append(v1) # 방향 표시가 없는 경우 양방향으로 표현해줌

bfs(1,V)

# 문제 예시 : 1에서 각 정점까지의 최소 거리의 합은?? (거리 = 간선 수)