def cal_synergy(li):
    total = 0
    
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            total += arr[li[i]][li[j]] + arr[li[j]][li[i]]
    return total

def get_synergy():
    A_list, B_list = [], []
    for i in range(N):
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)
    
    return cal_synergy(A_list), cal_synergy(B_list)

# 종료 조건 : 재료의 반을 선택 --> 시너지 계산
# 가지의 수 : 모든 재료(N)
def recur(count, prev):
    global answer
    if count == N // 2:
        # TODO 시너지 계산
        a_total, b_total = get_synergy()
        answer = min(answer, abs(a_total - b_total))

        return
    
    for food_number in range(prev, N):
        if visited[food_number] == 1: # 이미 쓴 재료는 안 쓴다.
            continue
        
        visited[food_number] = 1
        recur(count + 1, food_number + 1)
        visited[food_number] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    
    answer = 21e8

    recur(0, 0)
    print(f'#{tc} {answer}')