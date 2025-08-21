# from collections import deque

# T = 10
# for tc in range(1, T+1):
#     int(input())
#     # numbers = list(map(int, input().split()))
#     dq = deque(map(int, input().split()))
#     # dq = deque()
#     # dq.append(numbers)

#     while True:
#         for i in range(1, 6):
#             num = dq.popleft()
#             result = num - i

#             if result <= 0:
#                 dq.append(0)
#                 break
#             else:
#                 dq.append(result)
#         else:
#             continue
#         break
    
#     print(f'#{tc}', *dq)


from collections import deque

T = 10

for _ in range(1, T+1):
    tc = int(input())
    q = deque(map(int, input().split()))
    
    count = 1
    
    while q[7] > 0:
        a = q.popleft()
        if a - count <= 0:
            q.append(0)
            break
        else:
            q.append(a - count)

        count = (count) % 5 + 1
 
 
    print (f'#{tc}',*q)









