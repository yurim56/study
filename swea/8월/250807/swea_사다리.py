# 사다리
# 선형 탐색 - 가는 길이 하나로 정해져 있기 때문에
# 도착지에서 출발지를 찾아가기
# 올라가다가 수평으로 뚫려 있으면 가면 됨

# 상, 좌, 우
dr = [-1, 0, 0]
dc = [0, -1, 1]

# 위 -> 좌우 살피고 위 [1, 2, 0]
# 좌 -> 위 살피고 없으면 자기 자신 [0, 1]
# 우 -> 위 살피고 없으면 자기 자신 [0, 2]

search_dir = [[1,2,0], [0,1], [0, 2]]

T = 10
for tc in range(1, T+1):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    c = ladder[99].index(2)
    dir = 0

    # 이동 횟수를 모르면 while
    while r > 0:
        # 다음 방향 탐색
        for i in range(len(search_dir[dir])):
            # 다음 방향 후보
            next_dir = search_dir[dir][i]
            next_r = r + dr[next_dir]
            next_c = c + dc[next_dir]

            # r 좌표의 범위를 고민할 필요 없음
            if 0 <= next_c < 100 and ladder[next_r][next_c] == 1:
                dir = next_dir
                r = next_r
                c = next_c
                break

    print(f'#{tc} {c}')
