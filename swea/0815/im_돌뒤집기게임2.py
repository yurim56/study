T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

    # 1차원 델타배열(왼쪽, 오른쪽)
    dx = [-1, 1]

    for _ in range(M): # 뒤집기 횟수
        center, j = map(int, input().split())
        center -= 1 # 인덱스 조정

        for k in range(1, j + 1): # k는 퍼저나가는 파워
            left = center + dx[0] * k
            right = center + dx[1] * k

            # 범위 체크 (범위 벗어나면 안된다), 왼쪽돌과 오른쪽돌이 같은돌이면 뒤집기
            if 0 <= left and right < N and stones[left] == stones[right]:
                stones[left] = 1 - stones[left]
                stones[right] = 1 - stones[right]

    print(f'#{tc}', *stones)