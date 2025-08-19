# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     word = [list(map(int, input().split())) for _ in range(N)]

#     r = 0
#     c = 0
#     for i in range(N-K+1):
#         count = 0
#         for j in range(N-K+1):
#             for p in range(i, i+K):

# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     count = 0
#     for i in range(N):
#         len_cnt = 0
#         for j in range(N):
#             if arr[i][j] == 1:
#                 len_cnt += 1
#             else:
#                 if len_cnt == K:
#                     count += 1
#                 len_cnt = 0
#             if j == N - 1 and len_cnt == K:
#                 count += 1
#     for j in range(N):
#         len_cnt = 0
#         for i in range(N):
#             if arr[i][j] == 1:
#                 len_cnt += 1
#             else:
#                 if len_cnt == K:
#                     count += 1
#                 len_cnt = 0
#             if i == N - 1 and len_cnt == K:
#                 count += 1
                 
#     print(f'#{tc} {count}')



T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0  # 최종 결과 값
    for i in range(N): # 가로 행
        count_1 = 0 # 한 줄에 1이 3개 연속으로 있나 확인
        for j in range(N):
            if arr[i][j] == 1:
                count_1 += 1
            else:
                if count_1 == K:
                    answer += 1
                count_1 = 0
            if j == N-1 and count_1 == K:
                answer += 1

    for j in range(N): # 가로 행
        count_1 = 0 # 한 줄에 1이 3개 연속으로 있나 확인
        for i in range(N):
            if arr[i][j] == 1:
                count_1 += 1
            else:
                if count_1 == K:
                    answer += 1
                count_1 = 0
            if i == N-1 and count_1 == K:
                answer += 1

    print(f'#{tc} {answer}')




