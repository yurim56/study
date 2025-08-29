N = int(input())

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

graph = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

count = 0

def dfs(r, c):
    global count
    visited[r][c] = 1
    count += 1
    
    # 델타 배열을 사용해 4방향 재귀 호출
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == 1 and visited[nr][nc] == 0:
            dfs(nr, nc)
    return count

# 메인 로직 시작

li = []
for r in range(N):
    for c in range(N):
        # 아직 방문하지 않은 '1'을 발견하면
        if graph[r][c] == 1 and visited[r][c] == 0:
            count = 0
            li.append(dfs(r, c))
            
# 최종 결과 출력
print(len(li))
li.sort()
for num in li:
    print(num)