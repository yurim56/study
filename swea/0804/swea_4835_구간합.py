T = int(input())

for tc in range(1, T+1):
  N,M = map(int, input().split())
  numbers = list(map(int, input().split()))
  
  list1 = []

  for j in range(N-M+1):
    total = 0
    for sum_num in range(j, j+M):
      total += numbers[sum_num]
    list1.append(total)

  print(f'#{tc} {max(list1) - min(list1)}')