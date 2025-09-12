# 종료 조건 : N명의 모든 점원을 고려했을 때
#   - 가지치기 : 이미 높이가 선반 B 이상이면 더 이상 쌓을 필요 없음
# 가지의 수 : 
#   - 점원을 탑에 포함 시키는 경우 or 안시키는 경우

def recur(count, total_height): # count -> 인덱스 값이라고 생각
    global min_answer
    if total_height >= B: # 가지치기
        min_answer = min(min_answer, total_height)
        return 
    
    if count == N:
        return
    
    # 가지치기 할 때 전체 먼저 생각하고 그 다음에 가지치기
    recur(count + 1, total_height + heights[count]) # 탑에 포함 시키는 경우
    recur(count + 1, total_height) # 탑에 포함 시키지 않는 경우

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    
    min_answer = 200000 # 나올 수 있는 최대 범위 적기
    # 부분 집합 구하기
    recur()
    print(f'#{tc} {min_answer - B}')