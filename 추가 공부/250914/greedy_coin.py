# 동전의 최소 개수
# 큰 동전부터 나누자
coin_list = [10, 50, 100, 500]
target = 1730
result = 0

coin_list.sort(reverse=True)

for coin in coin_list:
    possible_cnt = target // coin
    result += possible_cnt
    target -= coin*possible_cnt

print(result)