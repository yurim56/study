paper = [[0]*100 for _ in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    for r in range(y, y+10):
        for c in range(x, x+10):
            paper[r][c] = 1

black_area = 0
for r in range(100):
    black_area += sum(paper[r])

print(black_area)

# black_area = 0
# for r in range(100):
#     for c in range(100):
#         if paper[r][c] == 1:
#             black_area += 1
