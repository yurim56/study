def road(x, y, count, distance):
    global answer
    if count == N: # 사과 N개를 모두 수확했으면 
        result = distance + x + y # 모든 사과를 수확했을 때 : 거리 + x + y
        answer = min(answer, result)
        return
    
    for i in range(N):
        if visited[i] == 0: # 사과를 수확하지 않았을 때만 시작
            visited[i] = 1
            road(apple[i][0], apple[i][1], count + 1, distance + abs(x-apple[i][0]) + abs(y-apple[i][1]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    apple = []
    visited = [0]*N
    answer = 1e9 # 최소를 구하는거니까 매우 큰 값 넣어주기

    for _ in range(N):
        x, y = map(int, input().split())
        apple.append((x, y))

    # print('apple :', apple)

    road(0, 0, 0, 0) # (시작_x, 시작_y, 사과 뽑은 수, 거리)

    print(f'#{tc} {answer}')



# 이 문제는 수업 시간에 했던 거를 그냥 외웠어서 외운 걸로 푸니까...답이 잘 안 나와요.....ㅜㅜ