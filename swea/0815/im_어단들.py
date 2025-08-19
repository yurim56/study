# T = int(input())

# for tc in range(1, T+1):
#    N, K = map(int, input().split())
#    arr = [list(map(int, input().split())) for _ in range(N)]

#    answer = 0

#    for r in range(N):
#      count = 0 # 행이 바뀔 때마다 초기화
#      for c in range(N):
#        if arr[r][c] == 1:
#          continue

#        if count == K:
#         answer += 1
#        count = 0
     
#      if count == K:
#        answer += 1

#    print(f'{tc} {answer}')


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # 가로(행) 방향으로 확인
    for r in range(N):
        count = 0
        for c in range(N):
            if arr[r][c] == 0:
                count += 1
            else:
                if count == K:
                    answer += 1
                count = 0
        if count == K: # 행의 끝이 '0'으로 끝나는 경우 처리
            answer += 1

    # 세로(열) 방향으로 확인
    for c in range(N):
        count = 0
        for r in range(N):
            if arr[r][c] == 0:
                count += 1
            else:
                if count == K:
                    answer += 1
                count = 0
        if count == K: # 열의 끝이 '0'으로 끝나는 경우 처리
            answer += 1
    
    print(f'#{tc} {answer}')