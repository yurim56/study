T = int(input())

def n_queen(row):
    global answer
    if row == N:
        answer += 1
        return
    
    for col in range(N):
        # 세로 검사 통과 & 좌하향 통과 & 우하향 통과
        if not col_visited[col] and not main_diag_visited[row-col+N-1] and not sub_diag_visited[row+col]:
            col_visited[col] = 1
            main_diag_visited[row-col+N-1] = 1
            sub_diag_visited[row+col] = 1

            n_queen(row+1)

            # 다시 원복하기
            col_visited[col] = 0
            main_diag_visited[row-col+N-1] = 0
            sub_diag_visited[row+col] = 0


for tc in range(1, T+1):
    N = int(input())

    col_visited = [0]*N # 0번 ~ N-1번 인덱스까지
    main_diag_visited = [0]*(2*N-1) # 좌하향 대각선 방문
    sub_diag_visited = [0] *(2*N-1) # 우하향 대각선 방문
    answer = 0

    n_queen(0)

    print(f'#{tc} {answer}')