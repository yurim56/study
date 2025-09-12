dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N*N+1)
    
    # 현재 위치 숫자 기준 상하좌우를 확인
    #   - 1 큰게 있으면 visited에 1이라고 체크
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                
                if arr[nr][nc] == arr[r][c] + 1:
                    # 현재 숫자는 다음으로 이동 가능
                    visited[arr[r][c]] = 1
                    break # 다른 방향은 볼 필요도 없음
                
        
    # 연속된 1의 개수가 가장 긴 곳을 찾는다
    max_count = 0 # 정답
    count = 0     # 하나하나마다 몇 개가 연속되는지?
    start = 0     # 숫자를 세기 시작한 위치
    for i in range(1, N*N+1):
        if visited[i] == 1:
            count += 1
        else: # 0을 만나면 계산
            if max_count < count:
                max_count = count # 초기화
                start = i - count
            count = 0
    
    print(f'#{tc} {max_count}')