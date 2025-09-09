for tc in range(1, 11):
    length = int(input())
    board = [input() for _ in range(8)]
 
    total = 0

    # 가로
    for i in range(8):
        for j in range(8 - length + 1):
            sub = board[i][j:j + length]
            if sub == sub[::-1]:
                total += 1

    # 세로
    for j in range(8):
        for i in range(8 - length + 1):
            vert = ""
            for k in range(length):
                vert += board[i + k][j]
            if vert == vert[::-1]:
                total += 1

    # 형식에 맞춰 결과를 출력합니다.
    print(f"#{tc} {total}")