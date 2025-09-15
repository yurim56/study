dr = [1, 0]
dc = [0, 1]

def dfs(r, c):
    global answer, total

    total += graph[r][c]

    if r == (N-1) and c == (N-1):
         answer = min(answer, total)

    else:
         for dir in range(2):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            dfs(nr, nc)

    total -= graph[r][c]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    answer = 10**9
    total = 0
    score = []

    dfs(0, 0)
    
    print(f'#{tc} {answer}')