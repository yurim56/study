for tc in range(1, 11):
    input()  # 테스트 케이스 번호 무시
    
    arr = [[0] * 100 for _ in range(100)]
    endR, endC = -1, -1

    # 입력 받기 및 지도 초기화
    for r in range(100):
        row = list(map(int, input().split()))
        for c in range(100):
            if row[c] == 1:
                arr[r][c] = 1
            elif row[c] == 2:
                arr[r][c] = 2
                endR, endC = r, c

    r, c = endR, endC

    # 위로 올라가면서 경로 추적
    while r > 0:
        if c - 1 >= 0 and arr[r][c - 1] == 1:  # 왼쪽으로 이동
            while c - 1 >= 0 and arr[r][c - 1] == 1:
                c -= 1
        elif c + 1 < 100 and arr[r][c + 1] == 1:  # 오른쪽으로 이동
            while c + 1 < 100 and arr[r][c + 1] == 1:
                c += 1
        r -= 1  # 위로 이동

    print(f"#{tc} {c}")


