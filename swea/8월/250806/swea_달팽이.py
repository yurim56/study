T = int(input())
 
di = [0, 1, 0, -1] 
dj = [1, 0, -1, 0]   
 
for tc in range(1, 1+T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    r, c = 0, 0
    dist = 0
 
    for n in range(1, N*N+1):
        arr[r][c] = n
        r+= di[dist]
        c+= dj[dist]
         
        if r < 0 or c < 0 or r>=N or c>=N or arr[r][c] != 0 :
            r-= di[dist]
            c-= dj[dist]
            dist = (1+dist)%4
 
            r+= di[dist]
            c+= dj[dist]
    print(f'#{tc}')
 
    for row in arr:
        print(*row)