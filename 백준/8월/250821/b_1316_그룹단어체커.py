# N = int(input())

# count = 0
# for _ in range(N):
#     word = input()

#     check = []
#     is_group_word = True
#     for i in word:
#         if i in check and check[-1] != i:
#             is_group_word = False
#             break            
        
#         if i not in check:
#             check.append(i)
    
#     if is_group_word:
#         count += 1

# print(count)


N = int(input())

count = 0
for _ in range(N):
    word = input()

    check = []
    for i in word:
        if i in check and check[-1] != i:
            break            
        
        if i not in check:
            check.append(i)
    
    else:
        count += 1

print(count)

# False True 사용법???