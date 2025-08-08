T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    flies = [list(map(int, input().split()))]
    answer = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            temp_sum = 0
            for i in range(M):
                for j in range(M):
                    temp_sum += flies[r+i][c+i] # 시작점으로부터 i,j만큼 떨어짐
            
            answer = max(answer, temp_sum)
            