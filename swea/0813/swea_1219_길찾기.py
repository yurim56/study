# for _ in range(10):
#     tc, total_len = map(int, input().split())
#     numbers = list(map(int, input().split()))

#     for i in numbers:
#         print(i, end=' ')


T = 10

def dfs(node):
    global answer

    if node == 99:
        answer = 1 # answer이 전역 변수이므로 global 사용

        return

    for next_node in adj_list[node]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)

for tc in range(1, T+1):
    _, M = map(int, input().split())
    info = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)] # 빈 리스트 100개 만들어주기
    answer = 0 # 발견하면 중단
    visited = [0]*100 # 해당 노드가 방문 했는 지를 판단하는 변수

    for i in range(M):
        a = info[2*i] # 출발지(짝수임)
        b = info[2*i+1] # 도착지(홀수)
        
        adj_list[a].append(b) # 유향 그래프 -> 한 쪽만 하면 됨
        # adj_list[b].append(a) 무향 그래프 -> 양 쪽 다 해줘야 함
    
    visited[0] = 1
    dfs(0) # 0번부터 시작
    