n = int(input())

# count = 0
# i = 0

# while True:
#     if n % 5 == 0:
#         count += n//5
#         break
    
#     else:
#         n -= 2
#         count += 1
    
#     if n < 0:
#         break

# if n < 0:
#     print(-1)
# else:
#     print(count)
    
    
# dp = [-1]*(n+8)
# dp[2] = 1
# dp[4] = 2
# dp[5] = 1
# dp[6] = 3
# dp[7] = 2
# dp[8] = 4

# for i in range(9, n+1):
#     dp[i] = min(dp[i-2], dp[i-5]) + 1

# print(dp[n])

if n in (1, 3):
    print(-1)

else:
    five = n // 5
    
    while five >= 0:
        rest = n - 5*five
        if rest %  2 == 0:
            two = rest // 2
            print(five + two)
            break
        
        five -= 1
    
    else:
        print(-1)