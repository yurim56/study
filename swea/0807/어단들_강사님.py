T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for r in range(N):
        count = 0 # 행이 바뀔 때마다 초기화 해주기
        for c in range(N):
            if graph[r][c] == 1:
                count += 1
                continue
            
            if count == K:
                answer += 1
            count = 0

            # else:                       위에랑 같은 뜻
            #     if count == K:
            #         answer += 1
            #     count = 0
        if count == K:
            answer += 1

    for c in range(N):
        count = 0 # 행이 바뀔 때마다 초기화 해주기
        for r in range(N):
            if graph[r][c] == 1:
                count += 1
                continue
            
            if count == K:
                answer += 1
            count = 0

            # else:                       위에랑 같은 뜻
            #     if count == K:
            #         answer += 1
            #     count = 0
        if count == K:
            answer += 1