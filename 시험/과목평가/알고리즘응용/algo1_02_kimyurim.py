# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))

#     answer = 0
    
#     # 1. 먼저 윈도우의 길이가 딱 M인 애들 먼저 찾기
#     # 전체 숫자에서 길이가 M인 윈도우가 만들어지는 수는 N//M개
#     for i in range(N//M): 
        
#         # 맨 앞에서부터 M번만큼 떨어진 곳으로 다음 번 로직이 시작 해야 함
#         front = i*M 
#         # print('================')
#         # print('front :', front)
#         window = numbers[front:front+M]
#         # print('window :', window)

#         # 증가하는 수열로 찾아야함
#         group = window[0] - 1
#         # print('group :', group)

#         for item in window:
#             if item <= group: # 해당 윈도우에서 증가하는 수열이 아닌 경우 멈춤
#                 break
#             group = item
#         else:
#             answer += 1
    
#     # 2. 맨 뒤에 하나의 윈도우 길이가 M이 아닌 경우가 있을 수 있기에 그 경우도 봐줌
#     back = (N//M)*M
#     # print('else_back : ', back)
#     window = numbers[back:back+M]
#     # print('else_window :', window)
#     if window:
#         group = window[0] - 1
#         for item in window:
#             if item <= group:
#                 break
#             group = item
#         else:
#             answer += 1

#     print(f'#{tc} {answer}')
#     # print('--------Next-------')

def is_increase(arr):
    before = -101               # -101로 한 이유 : 
    for i in range(len(arr)):
        if arr[i] > before:
            continue
        else:
            return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = 0
    
    K = N//M
    if N%M > 0:
        K += 1

    for count in range(K):
        idx = count * M
        answer += is_increase(numbers[idx:idx+M])
    
    print(f'#{tc} {answer}')