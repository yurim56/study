coins = [10, 50, 100, 500, 1000, 5000, 10000, 50000]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    target = N
    result = []

    coins.sort(reverse=True)

    for coin in coins:
        coin_num = target // coin
        target -= coin_num * coin
        result.append(coin_num)

    print(f'#{tc}')
    print(*result)