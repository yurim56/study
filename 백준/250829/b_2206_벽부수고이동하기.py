from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, -1]

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]

def bfs():
    que = deque()
    visited[0][0][0] = 1
    que.append((0, 0, 0)) # 처음: 벽 부순 횟수, 두 번째: r, 세 번째: c

    step = 1 # 처음과 끝을 포함한 경로의 수를 구하는 것이기게 step = 1

    while que:
        for _ in range(len(que)):
            k, r, c = que.popleft()

            if r == N-1 and c == M-1: # 끝 지점일 때
                return step # 만약 N, M이 1이면 바로 1이 출력됨

            for dir in range(4):
                nk = k
                nr, nc = r + dr[dir], c + dc[dir]            

                if nr < 0 or nr >= N or nc < 0 or nc >= N: # 그래프를 넘어가면
                    continue
                
                # 갈 수 있을 때?
                # if graph[nr][nc] == 1 and nk == 0:

                # elif graph[nr][nc] == 0: 이런 식으로 하면 else를 못 씀

                if graph[nr][nc] == 1:
                    if nk == 1 or visited[1][nr][nc]:
                        continue
                    nk = 1
                else:
                    if visited[nk][nr][nc]:
                        continue
                
                visited[nk][nr][nc] = 1
                que.append((nk, nr, nc))

        step += 1

    return -1

print(bfs())