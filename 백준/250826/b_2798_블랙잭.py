N, M = map(int, input().split())

numbers = list(map(int, input().split()))

answer = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if numbers[i] + numbers[j] + numbers[k] <= M:
                answer = max(numbers[i] + numbers[j] + numbers[k], answer)
            else:
                continue

print(answer)
