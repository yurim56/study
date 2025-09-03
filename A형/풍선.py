'''
정수 값이 적힌 N개의 풍선이 있다.
사용자는 N개의 총알로 모든 풍선을 한 번씩 터뜨려야 한다.

풍선을 터뜨릴 때마다, 해당 풍선의 좌우에 있던 풍선들이 인접하게 된다.
이때 점수는 다음 규칙에 따라 계산된다.

풍선을 터뜨릴 때: 

양쪽 풍선이 모두 남아 있으면: Bi-1 X Bi+1

왼쪽 풍선만 남아 있으면: Bi-1

오른쪽 풍선만 남아 있으면: Bi+1

좌우 모두 없으면(마지막 풍선): Bi

초기 점수는 0이며, 모든 풍선을 터뜨렸을 때 얻을 수 있는 점수의 최댓값을 구하라.

입력
 
첫 줄에 테스트케이스 개수 T가 주어진다.

각 테스트케이스에 대해:

첫 줄에 풍선의 개수 N(1≤N≤20)
둘째 줄에 N개의 정수 B1,B2,…,BN이 주어진다.

출력
각 테스트케이스마다 풍선을 터뜨려 얻을 수 있는 최대 점수를 출력한다.
 
입력
5
4
1 2 3 4
5
4 1 3 1 5
5
12 34 56 78 90
5
5 72 98 35 107
6
73 250 499 102 67 330

출력
#1 20
#2 57
#3 9360
#4 18939
#5 305580
'''

def dfs(rest, score):
    global answer
    
    # 길이 1일 때
    if len(rest) == 1:
        answer = max(answer, score+rest[0])
        return
    
    # 길이 2이상
    for i in range(len(rest)):
        if i == 0:
            dfs(rest[:i]+rest[i+1:], score+rest[1])
        elif i == len(rest)-1:
            dfs(rest[:i]+rest[i+1:], score+rest[i-1])
        else:
            dfs(rest[:i]+rest[i+1:], score+(rest[i-1]*rest[i+1]))

T = int(input())

for tc in range(1, T+1):
    answer = 0
    N = int(input())
    balloons = list(map(int, input().split()))
    visited = {}
    
    dfs(balloons, 0)
    
    print(f'#{tc} {answer}')