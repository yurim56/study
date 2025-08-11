T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    count_1 = 0
    max_v = 0


    for i in range(N):
        if arr[i] == 1:
            count_1 += 1
        elif arr[i] == 0:
            if max_v < count_1:
                max_v = count_1
            count_1 = 0

    if max_v < count_1:
        max_v = count_1
        
    print(f'#{tc} {max_v}')