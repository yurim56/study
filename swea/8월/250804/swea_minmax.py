T = int(input())

for tc in range(1, T+1):
  N = int(input())
  numbers = list(map(int, input().split()))
  min_num = numbers[0]
  max_num = numbers[0]

  for i in range(1,N):
   if min_num > numbers[i]:
    min_num = numbers[i]
   if max_num < numbers[i]:
    max_num = numbers[i]

  answer = max_num - min_num
  print(f'#{tc} {answer}')