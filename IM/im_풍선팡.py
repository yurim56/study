# dr = [-1, 1, 0, 0] # 상 하 좌 우
# dc = [0, 0, -1, 1]

# def get_score(r, c): # score 계산해서 그 결과를 달라
#     score = arr[r][c] # 초기화 - 현재좌표

#     for i in range(4): # 방향이 4방향이라서 (상, 하, 좌, 우)
#         nr, nc = r, c # 현재 위치
#         while True:
#             nr += dr[i]
#             nc += dc[i]
#             if 0 <= nr < N and 0 <= nc < N: 
#                 score += arr[nr][nc] # 점수계산
#             else: 
#                 break # 범위벗어나면 break

#     return score


# T = int(input())


# for tc in range(1, T + 1):
#     N = int(input()) # NcN 행렬
#     arr = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열
#     result = float('-inf')  # 최대값 초기화 (음의 무한대)

#     for r in range(N): # 행순회
#         for c in range(N):
#             # 함수호출하면서 최대값 갱신
#             # 함수 왜 만들까?? ---> 디버깅 때문에!!
#             temp = get_score(r, c)
#             result = max(result, temp)

#     print(f'#{tc} {result}') # 최대값 출력


dr = [-1, 1, 0, 0] # 상 하 좌 우
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]

  max_value = 0

  for r in range(N):
    for c in range(N):
      if arr[r][c] == 1:

        for i in range(4):
          count = 1
          nr, nc = r, c
          
          while 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
            count = 1
            nr = r + dr[i]
            nc = c + dc[i]