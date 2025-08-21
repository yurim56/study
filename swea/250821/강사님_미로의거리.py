from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = []
    answer = -1 # 거리 초기값 설정을 잘 해야함 

    s_r, s_c = -1, -1 # 시작 지점 찾기(없는 값으로)
    for r in range(N): # 행 위치 찾기
        temp = list(map(int, input())) # 2를 찾기 위해서
        for c in range(N): # 열 위치 찾기
            if temp[c] == 2:
                s_r, s_c = r, c
        
        graph.append(temp) # 그래프 생성
    
    # print(graph)

    visited = [[0]*N for _ in range(N)] # 방문 여부만 확인할 것 -> 0 or 1로만 표시해줌
    q = deque()
    q.append((s_r, s_c)) # 튜플로 사용하는 것이 리스트보다 좋음 -> 속도도 빠름
    visited[s_r][s_c] = 1

    flag = False # q에서 3이 발견되면 q에 있든 말든 상관없으니 끝내주겠다

    while q: # q가 빌 때까지 반복
        
        answer += 1 # 
        
        for _ in range(len(q)):
            r, c = q.popleft()

            for dir in range(4):
                nr = r + dr[dir]
                nc = c + dc[dir]

                # 1. 맵 안쪽이어야 한다
                # 2. 1이 아니어야 한다
                # 3. 방문 안 했어야 한다 -> 모두 and로 묶여야 함 == 하나라도 안 되면 안됨

                # 아래 조건 중 하나라도 만족하면 다음 방향을 보세요
                # 1. 맵 바깥쪽이거나
                # 2. 1이거나
                # 3. 방문 했거나
                if nr < 0 or nr >= N or nc < 0 or nc >= N or graph[nr][nc] == 1 or visited[nr][nc] == 1:
                    continue

                if graph[nr][nc] == 3:
                    flag = True
                    break

                # 셋 다 만족 안 함
                visited[nr][nc] = 1
                q.append((nr, nc))

            if flag:
                break
        if flag:
            break

    if not flag:
        answer = 0
    
    print(f'#{tc} {answer}')