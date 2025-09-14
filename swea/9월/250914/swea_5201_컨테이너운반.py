T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort()
    truck.sort()

    answer = 0

    while weight and truck:
        if weight[-1] <= truck[-1]:
            answer += weight.pop()
            truck.pop()
        else:
            weight.pop()
    
    print(f'#{tc} {answer}')