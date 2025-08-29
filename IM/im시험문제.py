T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pi_nums = list(map(int, input().split()))

    count = 0
    room_number = []
    for i in range(1, N+1):
        room_number.append(i)
    count += (N-1)
    
    left_num = 0
    for j in pi_nums:
        if j != 0:
            left_num += 1
    count += left_num

    minus_num = []
    for k in range(len(room_number)):
        minus_num.append(k+1 - pi_nums[k])

    minus = minus_num[1:len(minus_num)-1]
    
    fin = sum(minus)
    count += fin

    print(f'#{tc} {count}')