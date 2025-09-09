T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] # N X N 배열 입력 받기
    max_value = 0
    for i in range(N-M+1):         # 행 순회(N-M+1인 이유는 그 배열을 벗어나면 안되니까!!)
        for j in range(N-M+1):     # 열 순회
            max_sum = 0            # M X M 배열 원소들의 최대 합
            for p in range(i, i+M):          # 부분 배열의 행
                for q in range(j, j+M):      # 부분 배열의 열
                    max_sum += arr[p][q]
            max_value = max(max_value, max_sum)
                    
    print(f'#{tc} {max_value}')
    