'''
지도 - 이차원 배열 형태

맨홀 뚜껑으로부터 출발
    - 터널들을 이동
        - 이동 방향 : 상하좌우 -> 델타 배열
        - 이동 못하는 경우 존재
            - 현재 내 위치에서 뚫려 있는 곳만 이동 가능
            - 다음 위치의 입구가 뚫려 있는 곳으로만 가능
    - 시작점부터 주변으로 점점 퍼져나가면서 확인(BFS)
    - BFS : 큐를 활용해서 먼저 확인하는 노드부터 먼저 확인하자!
            먼저 방문한 노드에서 갈 수 있는 노드들을 후보군(큐)에 추가
        - 시간 복잡도

        1. BFS로 접근
            - 이동 방향 : 상하좌우
            - 이동이 불가능한 케이스
                - [델타 배열 기본] 범위 밖으로 나가면 못 감
                - [방문 기록 기본] 이미 방문한 곳은 못 감
                    - 0이면 못 간다
                - [문제 조건]
                    - 현재 내 위치에서 뚫려 있는 곳만 이동 가능
                    - 다음 위치의 입구가 뚫려 있는 곳으로만 가능
                    -> 이런 케이스들은 델타 배열과 동일한 순서(상하좌우)
                            - 이동 가능 여부 기록해두면 좋다.
        
        2. 방문 기록을 해야한다 (visited)
'''
from collections import deque

# 델타 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 터널들의 종류에 따라, 이동 가능 여부를 기록
types = {
    # 상하좌우 순서로 기록
    1 : [1, 1, 1, 1],
    2 : [1, 1, 0, 0],
    3 : [0, 0, 1, 1],
    4 : [1, 0, 0, 1],
    5 : [0, 1, 0, 1],
    6 : [0, 1, 1, 0],
    7 : [1, 0, 1, 0]
}

def bfs(R, C):
    que = deque([(R, C)]) # 후보군
    visited[R][C] = 1 # 출발점 초기화
    
    while que:  # 후보군이 없을 때까지(더 이상 방문할 수 있는 곳이 없으면 종료)
        r, c = que.popleft()
        dirs = types[graph[r][c]]
        
        for dir in range(4): # 상하좌우 확인
            # 출구가 없으면 다음 방향 확인 -> continue
            if dirs[dir] == 0:
                continue
            
            # 다음 좌표
            nr = r + dr[dir]
            nc = c + dc[dir]
          
            # 범위 밖이면 pass
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            
            # 못가는 곳이면 pass
            if graph[nr][nc] == 0:
                continue
            
            # 이미 방문했으면 pass
            if visited[nr][nc]:
                continue
            
            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[graph[nr][nc]]
                        
            # 현재 상좌 -> next_dirs의 하우가 안 뚫렸으면 못 간다
            if dir % 2 == 0 and next_dirs[dir+1] == 0:
                continue
            
            # 현재 하우 -> next_dirs의 상좌가 안 뚫렸으면 못 간다
            if dir % 2 == 1 and next_dirs[dir-1] == 0:
                continue
            
            # 시간을 +1 해주면서 기록
            visited[nr][nc] = visited[r][c] + 1
            que.append((nr, nc))
            
T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 방문 여부에 특정 좌표까지 몇 시간이 걸렸는 지 기록
    visited = [[0]*M for _ in range(N)]
    
    bfs(R, C) # 출발지를 시작으로 bfs 돌려줌
    count = 0
    
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                count += 1
    
    print(f'#{tc} {count}')