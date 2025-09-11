N = int(input())

events = []
for _ in range(N):
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    
    events.append((start, 1))
    events.append((end, -1))

events.sort(key=lambda x: (x[0], -x[1]))

cur = ans = 0

for _, d in events:
    cur += d
    if cur > ans:
        ans = cur

print(ans)