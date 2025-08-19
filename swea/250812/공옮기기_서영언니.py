T = int(input())

# 방향(우 하 좌 상)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    balls = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 1

    for x in range(N):
        for y in range(N):
            cnt = 1 # 칸수(시작칸 포함이라 +1)
            i = x
            j = y
            # 이동 못할때까지 이동하는 반복문
            while True:
                smaller = []
                smaller_idx = []
                #가는 상황에서 범위 안에 있을 때
                    #for -> 한 위치마다 네방향 탐색
                for delta in range(4):
                    ni = i + di[delta]
                    nj = j + dj[delta] 

                    # 자기보다 작은 값이 있으면 그 방향으로 이동 -> 가장 작은 값으로 이동
                    if 0<=ni<N and 0<=nj<N and balls[ni][nj] < balls[i][j]:
                        smaller.append(balls[ni][nj]) #값 저장
                        smaller_idx.append(delta) #방향저장

                #리스트 비어있으면 더 이동 불가하다는 뜻(반복문 탈출)              
                if len(smaller) == 0:
                    break
                
                # 가장 작은 값을 찾아서 거기 방향을 뽑고 이동 후 이동횟수 +1
                move = min(smaller)
                move_idx = smaller_idx[smaller.index(move)]
                i = i + di[move_idx]
                j = j + dj[move_idx]                  
                cnt += 1
                
            # 이동이 끝나고 이동횟수 비교 후 더 크면 최댓값 갱신    
            if cnt > max_cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')


    #1. 더 이상 움직일 수 없을 때까지
    #2. 자기 자리에서 4방향 탐색하여 자기보다 작으면 값 저장
    #3. 그 값들 중 가장 큰 값이 있는 곳으로 이동 (카운트 +1)
    #4. 이 값이 max_count보다 큰지 비교해서 크면 변경