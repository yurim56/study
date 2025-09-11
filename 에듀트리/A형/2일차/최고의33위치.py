dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for r in range(N-3+1):
    for c in range(N-3+1):
        plus = 0
        for i in range(3):
            for j in range(3):
                plus += graph[r + i][c + j] # 시작점 이동해주기!!!
        answer = max(answer, plus)
print(answer)