# # N = int(input())
# # people = list(map(int, input().split()))
# # adj_list = [[] for _ in range(N+1)]

# # for _ in range(N):
# #     arr = list(map(int, input().split()))
# #     num = arr[0]
# #     neighbors = arr[1:]
# #     adj_list.append(neighbors)
# #     # print('num :', num)
# #     # print('neighbors :', neighbors)


# from collections import deque
# from itertools import combinations

# def bfs(section):
#     q = deque([section[0]])
#     visited = {section[0]}
#     section_set = set(section)
#     while q:
#         now = q.popleft()
#         for nxt in graph[now]:
#             if nxt in section_set and nxt not in visited:
#                 visited.add(nxt)
#                 q.append(nxt)
#     return len(visited) == len(section)

# n = int(input())
# popularity = list(map(int, input().split()))
# graph = {}
# for i in range(n):
#     a = list(map(int, input().split()))
#     graph[i+1] = a[1:]

# tot = sum(popularity)
# ans = float('inf')  # 초기값을 inf로 설정

# for r in range(1, n//2 + 1):
#     for comb in combinations(range(1, n+1), r):
#         a = list(comb)
#         b = [x for x in range(1, n+1) if x not in a]

#         if bfs(a) and bfs(b):
#             popA = sum(popularity[x-1] for x in a)
#             popB = tot - popA
#             ans = min(ans, abs(popA - popB))

# print(ans if ans != float('inf') else -1)




di=[0,1,0,-1]
dj=[1,0,-1,0]

number=1
def dfs(row,col):
    visited[r][c]=1
    global number

    for dir in range(4):
        nr=row+di[dir]
        nc=col+dj[dir]

        if 0<=nr<N and 0<=nc<N:
            if house[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc]=1
                house[nr][nc]=number
                dfs(nr,nc)

N=int(input())
house=[list(map(int,input())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
answer=0

for r in range(N):
    for c in range(N):
        if house[r][c] == 1 and visited[r][c]==0: 
            dfs(r,c) #집에 1이 있고 방문안했으면 재귀함수 실행 
            house[r][c] = number
            answer+=1
            number+=1
            tot=0
            for row in visited:
                tot+=row.count(1)
            print(tot)

print(answer)