dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(row, col):
    visited[row][col] = 1
    house.append((row, col))

    for dir in range(4):
        nr = row + dr[dir]
        nc = col + dc[dir]

        if 0 <= nr < N and 0 <= nc < N:
            if graph[nr][nc] == 1 and visited[nr][nc] == 0:
                dfs(nr, nc)

N = int(input())

graph = [list(map(int, list(input()))) for _ in range(N)]


visited = [[0] * N for _ in range(N)]
house = []
fin_house = []
cluster = 0

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and visited[r][c] == 0:
            dfs(r, c)
            cluster += 1
            fin_house.append(len(house))
            house = []
print(cluster)
fin_house.sort()
for i in fin_house:
    print(i)