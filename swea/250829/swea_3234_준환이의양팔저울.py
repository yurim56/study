import math

def dfs(count, left, right): # count : 내가 고른 무게 추의 누적 개수
    global answer

    if left >= total_weight / 2:
        answer += 2**(N-count)*math.factorial(N-count)
        return


    if count == N:
        answer += 1 # 여기까지 온거면 경우의 수 하나 추가
        return # 탈출 조건이니까 return 필요
    
    for i in range(N):

        if visited[i]: # 방문 했으면
            continue

        visited[i] = 1
        dfs(count+1, left+weights[i], right) # 왼쪽 탐색

        if right+weights[i] <= left: # 오른쪽이 왼쪽 이하일 때만
            dfs(count+1, left, right+weights[i])

        visited[i] = 0 # 원복해주기


T = int(input())

for tc in range(1, T+1):
    answer = 0 # 경우의 수가 생길 때마다 누적해주기
    
    N = int(input())
    weights = list(map(int, input().split()))
    total_weight = sum(weights)
    visited = [0]*N # weights도 0번부터 N-1번까지 인덱스이니까 순서 맞춰주기

    dfs(0, 0, 0) # 처음 상태


#######################################################################################
# DP로 풀기

def dfs(count, diff):
    global visited

    if dp[visited].get(diff):
        return dp[visited][diff]

    if count == N: # 탈출 조건
        dp[visited][diff] = 1
        return dp[visited][diff]
    
    case_count = 0
    for i in range(N):
        if visited & (1 << i):
            continue

        visited |= (1 << i)
        case_count += dfs(count+1, diff+weights[i])

        if diff-weights[i] >= 0:
            case_count += dfs(count+1, diff-weights[i])
        
        visited ^= (1 << i)

    dp[visited][diff] = case_count
    return dp[visited][diff]


T = int(input())

for tc in range(1, T+1):
    answer = 0

    N = int(input())
    weights = list(map(int, input().split()))

    dp = [{} for _ in range(2**9)]
    
    visited = 0

    answer = dfs(0, 0)