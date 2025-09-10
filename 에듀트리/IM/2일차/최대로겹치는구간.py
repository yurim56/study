N = int(input())

lines = [tuple(map(int, input().split())) for _ in range(N)]    

max_end = 0
for start, end in lines:
    max_end = max(max_end, start, end)

count = [0] * (max_end+1)
for start, end in lines:
    for i in range(start, end+1):
        count[i] += 1

print(max(count))