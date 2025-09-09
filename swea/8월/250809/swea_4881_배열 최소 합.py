T = int(input())

for tc in range(1, T+1):
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]

  min_arr = []

  for i in arr:
    min_num = min(i)
    min_arr.append(min_num)

  print(f'#{tc} {sum(min_arr)}')