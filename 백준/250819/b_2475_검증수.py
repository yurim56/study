number = list(map(int, input().split()))

sqrt_num = []
for i in number:
    sqrt = i**2
    sqrt_num.append(sqrt)
    
print(sum(sqrt_num)%10)