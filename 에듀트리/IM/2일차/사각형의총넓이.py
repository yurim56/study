N = int(input())

lines = [tuple(map(int, input().split())) for _ in range(N)]    

visited = [[0]*201 for _ in range(201)]

for x1, y1, x2, y2 in lines:
    for x in range(x1, x2):
        for y in range(y1, y2):
            visited[x+100][y+100] = 1

answer = 0
for x in range(201):
    for y in range(201):
        answer += visited[x][y]

print(answer)