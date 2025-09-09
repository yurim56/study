N, M = map(int, input().split())


sunsae = []
for i in range(1, N+1):
    sunsae.append(i)

for _ in range(M):
    i, j = map(int, input().split())
    sunsae[i-1:j] = sunsae[i-1:j][::-1]

print(*sunsae)