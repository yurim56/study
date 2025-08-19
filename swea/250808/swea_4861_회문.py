T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = ''

    for i in arr:
        for j in range(N-M+1):
            check = i[j:j+M]
            if check == check[::-1]:
                result = check
                break
        
    if not result:
        for i in zip(*arr):
            for j in range(N-M+1):
                check = i[j:j+M]
            if check == check[::-1]:
                result = check
                break

    print(f'#{tc} {"".join(result)}')
