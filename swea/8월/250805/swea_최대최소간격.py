T = int(input())

for tc in range(1, T+1):
  N = int(input())
  numbers = list(map(int, input().split()))

  max_idx = 0
  min_idx = 0
  for i in range(1, N):
    if numbers[max_idx] <= numbers[i]:
      max_idx = i

    if numbers[min_idx] > numbers[i]:
      min_idx = i

  print(abs(max_idx - min_idx))
  print(f'#{tc} {abs(numbers[max_idx] - numbers[min_idx])}')