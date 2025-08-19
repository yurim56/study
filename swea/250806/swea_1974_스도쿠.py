# a = [
#     [7,3,6,4,2,9,5,8,1],
#     [5,8,9,1,6,7,3,2,4],
#     [2,1,4,5,8,3,6,9,7],
#     [8,4,7,9,3,6,1,5,2],
#     [1,5,3,8,4,2,9,7,6],
#     [9,6,2,7,5,1,8,4,3],
#     [4,2,1,3,9,8,7,6,5],
#     [3,9,5,6,7,4,2,1,8],
#     [6,7,8,2,1,5,4,3,9]
#     ]

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = True

    for i in range(len(arr)):        # 행끼리 검사
        set_1 = set()                # 셋에 넣어 길이가 9인지 확인
        for j in range(len(arr)):
            set_1.add(arr[i][j])
        if len(set_1) != 9:
            flag = False
    if flag:
        for p in range(len(arr)):        # 열끼리 검사
            set_2 = set()
            for q in range(len(arr)):
                set_2.add(arr[q][p])
            if len(set_2) != 9:
                flag = False
                break

    if flag:
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                set_3 = set()
                for x in range(r, r+3):
                    for y in range(c, c+3):
                        set_3.add(arr[x][y])
                if len(set_3) != 9:
                    flag = False
                    break

    if flag:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')