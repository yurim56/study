dr = [0, 1]
dc = [1, 0]

N = int(input())

def dfs(r, c):
    global answer
    
    if r == N-1 and c == N-1:
        answer = 'HaruHaru'
        return

    a = graph[r][c]
    
    if a == 0:
        return
    
    for dir in range(2):
        nr = r + dr[dir] * a
        nc = c + dc[dir] * a
        
        if 0 > nr or nr >= N or 0 > nc or nc >= N:
            continue
        
        dfs(nr, nc)
        
graph = [list(map(int, input().split())) for _ in range(N)]

answer = 'Hing'

dfs(0,0)
print(answer)