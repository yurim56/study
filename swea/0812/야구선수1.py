T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    stats = list(map(int, input().split())) # 실력
    
    answer = 1 # 팀원이 1명인 경우는 없음

    # 2명 이상 팀일 경우 생각하기
    stats.sort() # sorted(stats) -> 얘는 정렬 값을 새로 저장해준다는 것

    # 첫 번째 기준점 (N-1번까지 보면 팀원이 1명이기에 볼 필요가 X)
    for i in range(N-1):
        temp = 1 # 몇 명의 팀원을 봤는 지 누적하는 변수 -> j가 통과되면 +1을 해줌 -> 근데 그게 2 이상이어야 하니까 초기값 = 1
        for j in range(i+1, N): # i부터 보면 팀원 i==j 가 되어 팀원 1명이 됨
            if stats[j] - stats[i] > K: # K를 넘어가면 중단할 것
                break

            temp += 1
        answer = max(answer, temp)
    
    print(f'#{tc} {answer}')