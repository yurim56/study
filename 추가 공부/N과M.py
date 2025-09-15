numbers = [1,2,3,4,5]
N = 5
picked = []
count = 0

# def dupli_perm(cnt):
#     if cnt == N:
#         print(picked)
#         return
    
#     for i in range(len(numbers)):
#         picked.append(numbers[i])
#         dupli_perm(cnt+1)
#         picked.pop()

# visited = [0] * len(numbers)
# def perm(cnt):
#     if cnt == N:
#         print(picked)
#         return
    
#     for i in range(len(numbers)):
#         if visited[i] == 0:        
#             picked.append(numbers[i])
#             visited[i] = 1
#             perm(cnt+1)
#             picked.pop()
#             visited[i] =0
# perm(0)

print('=======================================')
def comb(cnt, idx):
    # print(picked)
    if cnt >=2:
        count+=1
        return
    
    for i in range(idx, len(numbers)):
        picked.append(numbers[i])
        comb(cnt+1, i+1)
        picked.pop()
        
comb(0,0)
