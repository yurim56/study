T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 2:
                start_r, start_c = r, c
                break
    
    stack = [(start_r, start_c)]
    visited[start_r][start_c] = 1
    result = 0

    while stack:
        curr_r, curr_c = stack.pop()

        if graph[curr_r][curr_c] == 3:
            result = 1
            break

        for dir in range(4):
            nr = curr_r + dr[dir]
            nc = curr_c + dc[dir]

            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] != 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                stack.append((nr, nc))
    
    print(f'#{tc} {result}')