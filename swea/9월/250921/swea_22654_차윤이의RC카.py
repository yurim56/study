T = int(input())

# 시계방향 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())
    graph = [list(input()) for _ in range(N)]
    Q = int(input())
    
    sr = sc = er = ec = -1

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 'X':
                sr, sc = r, c
            elif graph[r][c] == 'Y':
                er, ec = r, c

    result = []
    for _ in range(Q):
        C, cmd = input().split()

        r, c = sr, sc
        d = 0
        
        for ch in cmd:
            if ch =='L':
                d = (d-1)%4
            elif ch == 'R':
                d = (d+1)%4
            else:
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] != 'T':
                    r, c = nr, nc

        if r == er and c == ec:
            result.append('1')
        else:
            result.append('0')

        # result.append('1' if (r==er and c==ec) else '0')
    
    print(f"#{tc} {' '.join(result)}")