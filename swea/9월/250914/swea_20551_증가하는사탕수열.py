T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    eat = 0

    if B >= C:
        eat += B - (C - 1)
        B = C - 1
    
    if A >= B:
        eat += A - (B - 1)
        A = B - 1

    if A <= 0 or B <= 0 or C <= 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {eat}')