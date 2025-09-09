def dfs(x,y):
    global whitebug
    if 0<=y+1<M :
        if cabbage_lit[x][y+1]==1:
            dfs(x,y+1)
            return
    if 0<=y+1<M :
        if cabbage_lit[x+1][y]==1:
            dfs(x+1,y)
            return
    if 0<=y+1<M and 0<=x+1<N :
        if cabbage_lit[x][y+1] ==0 and cabbage_lit[x+1][y] == 0:
            whitebug +=1
            for i in range(x,N):
                for j in range(y,M):
                    if cabbage_lit[i][j] ==1 :
                        dfs(i,j)
                    else:
                        return

T = int(input())

for t in range(T):
    N , M , K = map(int,input().split())
    whitebug = 0
    cabbage_lit =[[0]*M for _ in range(N)]

    for i in range(K):
        cabbage = list(map(int,input().split()))
        cabbage_lit[cabbage[0]][cabbage[1]] = 1
    print(cabbage_lit)

    dfs(0,0)