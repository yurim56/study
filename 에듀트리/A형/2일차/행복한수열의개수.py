N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0

# 가로 탐색
for r in range(N):
    count = 1
    
    if M == 1:
        answer += 1
        continue
        
    for c in range(N-1):
        print(c)
        if graph[r][c] == graph[r][c+1]:
            count += 1
        else:
            count = 1
        
            break
        
# 세로 탐색
for c in range(N):
    count = 1
    
    if M == 1:
        answer += 1
        continue
        
    for r in range(N-1):
        if graph[r][c] == graph[r+1][c]:
            count += 1
        else:
            count = 1
        
            break

print(answer)