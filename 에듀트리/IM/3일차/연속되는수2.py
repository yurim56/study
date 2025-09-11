N = int(input())
arr = [int(input()) for _ in range(N)]

count = 1
max_count = 1

for i in range(N-1):
    if arr[i] == arr[i+1]:
        count += 1
    else:
        count = 1
    max_count = max(count, max_count)
    
print(max_count)