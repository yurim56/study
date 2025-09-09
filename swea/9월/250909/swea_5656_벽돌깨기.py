'''
1. 최소 벽돌
    - 현재 벽돌이 다 깨지면 더 이상 할 필요 없다  -> 현재 벽돌 수 관리
    

2. N번의 구슬을 굴려야 한다
    - 모든 케이스를 보아야 한다
    - 백트래킹
        - 한 번 쏘았을 때 벽돌들이 연쇄로 깨진다.
        - 현재 기준으로 퍼져나가면서 탐색 (BFS)
        - 빈칸 메우기
'''
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def shoot(count, remains, now_arr):
    global min_blocks
    # 종료 조건 : N개의 구슬을 모두 발사 or 남은 벽돌이 0이면
    if count == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return

    # 모든 열에 한 줄씩 떨구자
    for col in range(W):
        # 방법1. 원본을 복사해두고, 다시 되돌리는 방법
        # 1. col 위치에 떨구기 전 상태를 복사(얕은 복사 주의)
        # 2. 원본 리스트의 col 위치에 떨구고
        # 3. count + 1번 재귀 상태로 이동
        # 4. 떨구기 전 상태로 복구
        
        # 방법2. 복수 시간이 없는 방식
        # 1. 복사된 col 위치에 떨구기 전 상태를 복사
        # 2. 복사한 리스트의 col 위치에 떨군다.
        # 3. count + 1번 상태로 이동할 때, copy_arr을 함께 전달
        copy_arr = [row[:] for row in arr] 
        
        row = -1
        # 가장 위 벽돌을 검색
        for r in range(H):
            if arr[r][col]:
                row = r
                break
            
        if row == -1:  # 벽돌이 없는 열은 pass
            continue
        
        # 해당 row, col 의 숫자부터 시작해서 BFS
        # 행, 열, 숫자 모두 담아야 한다
        que = deque([(row, col, copy_arr[row][col])])
        now_remains = remains - 1
        copy_arr[row][col] = 0  # 구슬이 처음 만나는 벽돌 자기
        
        while que:
            r, c, p = que.popleft()
            for k in range(1, p):
                for i in range(4):
                    nr = r + (dr[i]*p)
                    nc = c + (dc[i]*k)

                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue
                    
                    # 벽돌이 없으면 pass
                    if copy_arr[nr][nc] == 0:
                        continue
                    
                    que.append((nr, nc, copy_arr[nr][nc])) # 다음 벽돌 추가
                    copy_arr[nr][nc] = 0                   # 벽돌 깨짐
                    now_arr -= 1                           # 숫자 감소


                
        # 주변 벽돌들을 순차적으로 파괴
        # 빈칸 메우기
        shoot(count + 1, now_remains, copy_arr)
        
T = int(input().split())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9 # 최소 벽돌 수
    blocks = 0
    
    # 남은 벽돌 수 
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1
    
    shoot()
    print(f'#{tc} {min_blocks}')