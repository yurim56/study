set_1 = set()

for _ in range(10):
    N = int(input())
    set_1.add(N%42)

print(len(set_1))