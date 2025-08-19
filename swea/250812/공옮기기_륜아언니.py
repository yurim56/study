
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]


    max_count = 0
    for i in range(N):
        for j in range(N):

            count = 1
            x, y = i, j
            
            while True:
                min_num = arr[x][y]
                x_move, y_move = -1, -1
                for m in range(4):
                    ni = x + di[m]
                    nj = y + dj[m]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] < min_num:
                            min_num = arr[ni][nj]

                            x_move = ni
                            y_move = nj

                max_count = max(max_count, count)
                
                if x_move == -1:
                    break
                else:
                    x, y = x_move, y_move
                    count += 1


    print(f"#{tc} {max_count}")