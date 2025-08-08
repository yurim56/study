# for tc in range(1, 11):
#     T = int(input())
#     lad = [list(map(int, input().split()))]

#     ladder = lad[::-1]

# for i in range(len(lad)):
#     for j in range(len(lad)):
#         print(lad[i][j], end=' ')
#     print()

# for i in range(len(ladder)):
#     for j in range(len(ladder)):
#         print(ladder[i][j], end=' ')
#     print()

# 0 : 상, 1 : 좌, 2 : 우
dr = [-1, 0, 0]
dc = [0, -1, 1]

# 0 : [1, 2, 0] -> '상'일 때는 좌, 우 보고 상 가기
# 1 : [0, 1]
# 2 : [0, 2]

search_dir = [[1, 2, 0], [0, 1], [0,2]]

T = 10
for tc in range(1, T+1):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 출구에서부터 거꾸로 올라가기
    r = 99
    c = ladder[99].index(2) # 마지막 줄의 위치 찾기

    dir = 0

    while r > 0:
        # 현재 방향에 따라 탐색 후보가 달라짐
        for i in range(len(search_dir[dir])):
            # 다음 방향 후보 (확정 아님)
            next_dir = search_dir[dir][i]
            next_r = r + dr[next_dir]
            next_c = c + dc[next_dir]

            # r좌표에 대한 범위는 생각 x -> 일단 아래로 가는 것 생각X
            #                          -> 위로는 while로 조건 줘서
            if 0 <= next_c < 100 and ladder[next_r][next_c] == 1:
                dir = next_dir
                r = next_r
                c = next_c
                break # 다음 방향을 탐색할 것이 없으니 break
    
    print(f'#{tc} {c}')