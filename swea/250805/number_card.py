T = int(input())

for tc in range(1, T+1):
  N = int(input())
  numbers = list(map(int,input()))
  cards = {0:0, 1:0, 2:0, 3:0, 4:0,
          5:0, 6:0, 7:0, 8:0, 9:0}
  
  for num in numbers:
    cards[num] += 1

  max_count = 0
  max_num = 0

  for i in range(10):
    if cards[i] >= max_count:
      max_count = cards[i]
      max_num = i
  print(f'#{tc} {max_num} {max_count}')