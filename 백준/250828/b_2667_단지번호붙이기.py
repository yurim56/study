N = int(input())

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

graph = [list(map(int, input())) for _ in range(N)]

count = 0

def dfs(r, c):
    # 유효성 검사: 범위, 바다('0') 여부
    if not (0 <= r < N and 0 <= c < N and graph[r][c] == 1):
        return 0

    # 방문했음을 표시하기 위해 '1'을 '0'으로 변경
    graph[r][c] = 0
    count = 1

    # 델타 배열을 사용해 4방향 재귀 호출
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        count += dfs(nr, nc)
    return count

# 메인 로직 시작

complexes = []
for r in range(N):
    for c in range(N):
        # 아직 방문하지 않은 '1'을 발견하면
        if graph[r][c] == 1:
            complexes.append(dfs(r, c))       # DFS로 해당 섬 전체를 방문 (지우기)

# 최종 결과 출력
print(len(complexes))
for count in sorted(complexes):
    print(count)