# # UDLR > 방향 전환 + (가능하면) 이동
# # S    > 포탄 쏘기(현 방향으로 쏘기 > 현 방향을 기억해놔야겠다)
# #        ~까지(밖에 나가거나, 벽(* 또는 #)에 부딪히거나)
# #        단, 그 벽이 벽돌벽(*)이면 거기 평지(.)로 바꿔야함

# # 상 : 0 , 하 : 1, 좌  : 2, 우 : 3
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# point_dir = {'^': 0, 'v': 1, '<': 2, '>': 3, 'U': 0, 'D': 1, 'L': 2, 'R': 3}
# tank_shape = ['^', 'v', '<', '>']

# T = int(input())

# for tc in range(1, T+1):

#     cur_dir = -1 # 현재 방향
#     cur_r = -1   # 현재 위치
#     cur_c = -1

#     H, W = map(int, input().split())
#     graph = []

#     # 입력 및 탱크 위치 파악
#     for r in range(H):
#         temp = list(input())
#         for c in range(W):
#             if temp[c] in ['<', '>', '^', 'v']:
#                 cur_r = r
#                 cur_c = c
#                 cur_dir = point_dir[temp[c]]
#         graph.append(temp)

#     input()
#     orders = input()

#     for order in orders:

#         # 방향 전환을 하고자 할 때
#         if order in ['U', 'D', 'L', 'R']:
#             cur_dir = point_dir[order]
            
#             nr = cur_r + dr[cur_dir]
#             nc = cur_c + dc[cur_dir]
            
#             if nr < 0 or nr >= H or nc < 0 or nc >= W or graph[nr][nc] != '.':
#                 continue
            
#             graph[cur_r][cur_c] = '.' 
#             cur_r = nr
#             cur_c = nc
#             graph[cur_r][cur_c] = tank_shape[cur_dir]

#         else:
#             while 0 <= cur_r < H and 0 <= cur_c < W:

#                 if graph[cur_r][cur_c] in ['*', '#']:
#                     if graph[cur_r][cur_c] == '*':
#                         graph[cur_r][cur_c] = '.'
#                     break

#                 cur_r += dr[cur_dir]
#                 cur_c += dc[cur_dir]

#     print(f'#{tc}', end=" ")
#     for i in range(H):
#         print(''.join(graph[i]))


T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
