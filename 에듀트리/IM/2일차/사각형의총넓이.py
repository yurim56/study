N = int(input())
sum = 0
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    square = (x2 - x1) * (y2 - y1)
    print(square)
    sum += square

print(sum)