T = int(input())

for tc in range(1, T+1):
    day, month, quarter, year = map(int, input().split())
    plans = list(map(int, input().split()))
    
    answer = year 
    
    dp = [0]*13 # why 13개?? -> 아무 것도 비용이 안 드는 시작점이 필요함
    dp[0] = 0 # 0 이전에는 달이 없어서 비용이 0임
    
    for i in range(1, 13):
        
        dp[i] = dp[i-1] + min(plans[i-1]*day, month)
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + quarter)
        
        if dp[i] >= answer:
            break
    
    else:
        answer = dp[12]
    
    print(f'#{tc} {answer}')