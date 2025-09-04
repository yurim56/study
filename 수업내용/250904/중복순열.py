# [0, 1, 2] 3개의 카드가 존재 -> 2개를 뽑는다.

path = []

# 기저 조건(종료 조건) : 2개의 카드를 모두 뽑았다면 종료
#   - 시작점 : 0개의 카드를 고른 상태부터 시작
# 다음 재귀 호출 구조 : [0, 1, 2] 카드 중 하나를 고른다.

def recur(count):
    if count == 2: # 기저 조건
        print(*path)
        return 

    # for num in range(3):
    #     path.append(num)
    #     recur(count + 1)
    #     path.pop()
    
    # 카드 0, 1, 2 중 하나를 선택
    path.append(0)
    recur(count + 1) # 하나 선택했으니 다음 선택으로 이동
    
    path.append(1)
    recur(count + 1)
    
    path.append(2)
    recur(count + 1)
    
recur(0)