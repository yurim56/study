N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

min_T = 0
for size in sizes:
    min_T += (size+T-1) // T

max_P = N // P
single_P = N % P

print(min_T)
print(max_P, single_P)