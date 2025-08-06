for tc in range(1, 11):
    t_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_row = 0
    for i in range(len(arr)):       # 행의 최댓값 찾기
        row_sum = 0

        for j in range(len(arr)):
            row_sum += arr[i][j]

        if max_row < row_sum:
            max_row = row_sum
        
    # print(max_row)

    max_col = 0
    for x in range(len(arr)):       # 열의 최댓값 찾기
        col_sum = 0
        for y in range(len(arr)):
            col_sum += arr[y][x]
        
        if max_col < col_sum:
            max_col = col_sum

    # print(max_col)

    dia_r_sum = 0
    for p in range(len(arr)):
        dia_r_sum += arr[p][p]

    # print(dia_r_sum)

    dia_l_sum = 0
    for r in range(len(arr)):
        dia_l_sum += arr[r][len(arr)-r-1]

    # print(dia_l_sum)

    print(f'#{tc} {max(max_row, max_col, dia_r_sum, dia_l_sum)}')