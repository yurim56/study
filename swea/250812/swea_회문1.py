T = 10

for tc in range(1, T+1):
    N = int(input())
    graph = [input() for _ in range(8)]
    answer = 0

    for i in range(8): # 행은 끝까지 가야함
        for j in range(8-N+1): # 열은 스킵 가능 -> 파리 퇴치와 유사

            for k in range(N//2): # 전체 길이의 절반
                if graph[i][j+k] != graph[i][j+N-1-k]: # -> 절반 돌아주겠다 N-1:끝글자로 감, k:반복수
                    break
            else:
                answer += 1

            for k in range(N//2): # 전체 길이의 절반
                if graph[j+k][i] != graph[j+N-1-k][i]: # -> 절반 돌아주겠다 N-1:끝글자로 감, k:반복수
                    break
            else:
                answer += 1
