'''
1. B를 C보다 작게
2. A를 B보다 작게
---------------------설계---------------------
완전 탐색부터 파악하기 -> 그 다음 규칙 세우기
완탐 -> B를 C보다 작을 때까지 하나씩 먹자 -> A를 B보다 작을 때까지 하나씩 먹자
     -> 너무 비효율적임
규칙 -> B = C - 1 / A = B - 1
'''

T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    
    # 불가능한 케이스를 먼저 지우자
    if A < 1 or B < 2 or C < 3:
        print(f'#{tc} -1')
        continue
    
    eat_count = 0
    
    # B상자 = C상자 -1
    if B >= C:
        eat_count += B - (C-1)
        B = C - 1
            
    # A상자 = B상자 -1
    if A >= B:
        eat_count += A - (B-1)
        A = B - 1
        
    print(f'#{tc} {eat_count}')