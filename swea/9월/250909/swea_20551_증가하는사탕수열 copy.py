T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    eat = 0
    
    if A < 1 or B < 2 or C < 3:
        print(f'#{tc} -1')
        continue
    
    if B >= C:
        eat += B - (C-1)
        B = C - 1

    if A >= B:    
        eat += A -(B-1)
        A = B - 1
    
    print(f'#{tc} {eat}')