N = 3 # 갖고 있는 데이터의 수
numbers = [1, 2, 3]
visited = [0]*N 

def subset(count):      # 진행되는 과정이 비선형이기에 재귀 함수 사용
    if count == N:
        # 여기서는 visited만 결정된 것
        for i in range(N):
            if visited[i]:
                print(visited, end = ' ')
        print()
        return
    
    subset(count+1)     # 그대로 [0,0,0]을 보내준 것, count 인덱스만 보낸 것
    visited[count] = 1  # [1,0,0]으로 만들어주기
    subset(count+1)     
    visited[count] = 0  # 다시 뒤로 돌아오기ㅏ

subset(0)