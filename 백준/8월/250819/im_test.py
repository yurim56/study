T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pi_nums = list(map(int, input().split()))

    count = 0
    
    # 방 번호를 리스트로 만들어주기
    room_number = []
    for i in range(1, N+1):
        room_number.append(i)
    
    # 처음 오른쪽으로 갈 때 더해주기
    count += (N-1)
    
    left_num = 0
    for j in pi_nums:
        if j != 0: # p[i]에서 0이 아닐 때
            left_num += 1
    
    # 왼쪽으로 가는 경우 더해주기
    count += left_num

    minus_num = []
    for k in range(len(room_number)):
        minus_num.append(room_number[k] - pi_nums[k]) # 이건 내가 공식 찾아서 방 번호에서 p[i] 번호 뺐어

    # 요건 1번방부터 N번방까지 쭉 뺀 건데, 1번이랑 N번은 필요 없으니까 그 사이에 있는 값들만 다시 구했어
    minus = minus_num[1:len(minus_num)-1]
    
    fin = sum(minus)
    
    # 다시 오른쪽으로 가는 경우 더해주기
    count += fin


    print(f'#{tc} {count}')
