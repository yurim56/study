dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1. 종료 조건 : 숫자 7자리일 때 종료
# 2. 가지의 수 : 4개 (상하좌우)
def recur(r, c, number):
    if len(number) == 7:
        result.add(number)
        return
    
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        
        # 범위 밖이면 continue
        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
            continue
        
        # 다음 위치로 이동만 하면 됨
        recur(nr, nc, number + graph[nr][nc]) # 문자열이라 덧셈이 가능

T = int(input())

for tc in range(1, T+1):
    graph = [input().split() for _ in range(4)]
    result = set() # 7자리 담아주기
    
    # 7자리 만드는 코드
    #   - 4 * 4가 모두 출발점이 될 수 있다 
    for start_r in range(4):
        for start_c in range(4):
            recur(start_r, start_c, graph[start_r][start_c])
    
    print(f'#{tc} {len(result)}')
    
    
    