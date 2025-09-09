def dfs(idx, fee):
    global answer

    if answer <= fee:
        return
    
    if idx >= 12: # 12가 넘어가는 경우도 있으니 생각해야함
        answer = min(answer, fee)
        return
    
    # ㄱ. 일권을 사는 경우
    dfs(idx+1, fee + day*plans[idx])
    
    # ㄴ. 월권을 사는 경우
    dfs(idx+1, fee + month)
    
    # ㄷ. 3개월권을 사는 경우    
    dfs(idx+3, fee + quarter)

T = int(input())

for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    plans = list(map(int, input().split()))
    
    # 최소비용 -> 일단 연간 이용권 값을 지정 
    #            why? 아무리 커도 연간 이용권보단 작아야 최소임
    answer = year 
    
    # ㄱ. 내가 몇 월의 의사결정을 하고 있는지
    # ㄴ. 해당 월 전까지의 누적 비용
    # 주의 : 월은 -1 처리해야 함 -> 인덱스 번호 맞춰주기
    
    dfs(0, 0) # 월, 돈
    
    print(f'#{tc} {answer}')