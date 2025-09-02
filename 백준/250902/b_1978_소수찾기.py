N = int(input())
numbers = list(map(int, input().split()))

count = 0
for num in numbers:
    if num == 1:
        continue
    div = 0
    for i in range(1, num+1):
        if num % i == 0:
            div += 1
    
    if div == 2:
        count += 1

print(count)