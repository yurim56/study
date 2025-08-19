T = int(input())

for tc in range(1, T+1):
  N = int(input())
  Ai = list(map(int, input().split()))
  Bi = list(map(int, input().split()))

  current = Ai[:]
  count = 0
  for i in range(N):
      if current[i] != Bi[i]: 
          count += 1
          for j in range(i, N): #i부터 N까지
            current[j] = 1 - current[j] # 1이면0 0이면1
 
  print(f'#{tc} {count}')

