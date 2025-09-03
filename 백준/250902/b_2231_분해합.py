N = int(input())

result = 0
for i in range(1, N+1):
    digits_sum = sum(map(int, str(i)))
    # print(f"i={i}, 자리수 합={digits_sum}, 분해합={i + digits_sum}")
    
    if i + digits_sum == N:
        result = i
        break

print(result)
