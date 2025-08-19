# T = int(input())

# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# for tc in range(1,T+1):
#   N = int(input())
#   snail = [[0]*N for _ in range(N)]

#   r = 0
#   c = 0
#   dir = 0

#   for number in range(1, N*N+1):
#     snail[r][c] = number
#     nr = r + dr[dir]
#     nc = c + dc[dir]

#     if 0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0:
#       r = nr
#       c = nc
      
#     else:
#       dir = (dir+1)%4
#       r += dr[dir]
#       c += dc[dir]

T = int(input())

dr_plus = [-1, 1, 0, 0]
dc_plus = [0, 0, -1, 1]
dr_cross = [-1, -1, 1, 1]
dc_cross = [-1, 1, -1, 1]

for tc in range(1, T+1):
  N,M = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]
  
  max_flies = 0

  for r in range(N):
    for c in range(N):
      plus_sum = arr[r][c]

      for i in range(4):
        for j in range(1, M):
          nr = r + dr_plus[i]*j
          nc = c + dc_plus[i]*j

          if 0 <= nr < N and 0 <= nc < N:
            plus_sum += arr[nr][nc]

      cross_sum = arr[r][c]
      for i in range(4):
        for j in range(1, M):
          nr = r + dr_cross[i]*j
          nc = c + dc_cross[i]*j

          if 0 <= nr < N and 0 <= nc < N:
            cross_sum += arr[nr][nc]

      if plus_sum > max_flies:
        max_flies = plus_sum
      if cross_sum > max_flies:
        max_flies = cross_sum

  print(f'{tc} {max_flies}')