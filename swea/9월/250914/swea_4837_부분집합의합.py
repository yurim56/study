# def subset(count):
#     global answer
#     if count == len(A):
#         if len(path) == N and sum(path) == K:
#             answer += 1
#             print(path)
#         return
    
#     if len(path) > N:
#         return
    
#     # if len(path) + (len(A) - count) < N:
#     #     return

#     path.append(A[count])
#     subset(count + 1)

#     path.pop()
#     subset(count + 1)

# T = int(input())
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     path = []
#     answer = 0

#     subset(0)
#     print(f'#{tc} {answer}')

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def subset(count, idx):
    global answer
    if count >= N:
        if sum(picked) == K and len(picked) == N:
            answer += 1
            print(picked)
        return

    if len(picked) >= N:
        return

    for i in range(idx, len(A)):
        picked.append(A[i])
        subset(count + 1, i + 1)
        picked.pop()

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    picked = []
    answer = 0

    subset(0, 0)
    print(f'#{tc} {answer}')