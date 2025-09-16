def synergy(team):
    # total: 시너지 합 L: 팀에 속한 사람 수
    total = 0
    L = len(team)
    
    for x in range(L):
        for y in range(x + 1, L):
            i, j = team[x], team[y]
            total += (arr[i][j] + arr[j][i])
    return total

# N개 중에 2개 뽑기
def recur(count, start):
    global answer
    if count == N // 2:
        other = []
        for i in range(N):
            if visited[i] == 0:
                other.append(i)

        diff = abs(synergy(pick) - synergy(other))
        if diff < answer:
            answer = diff
        return
    
    for i in range(start, N):
        if visited[i] == 1:
            continue

        visited[i] = 1
        pick.append(i)
        recur(count+1, i + 1)
        pick.pop()
        visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    answer = float('inf')
    visited = [0] * N
    pick = []

    # 0번을 팀 A에 고정해서 대칭 줄이기
    visited[0] = 1
    pick.append(0)

    
    recur(1, 1)
    print(f'#{tc} {answer}')


from itertools import combinations
import sys
input = sys.stdin.readline

def synergy(team, arr):
    s = 0
    for i, j in combinations(team, 2):
        s += arr[i][j] + arr[j][i]
    
    return s

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = float('inf')
    indices = list(range(N))

    for teamA in combinations(indices[1:], N//2 - 1):
        teamA = (0, ) + teamA
        teamB = []
        for i in indices:
            if i not in teamA:
                teamB.append(i)
        teamB = tuple(teamB)

        a = synergy(teamA, arr)
        b = synergy(teamB, arr)

        diff = abs(a-b)

        if diff < answer:
            answer = diff
    
    print(f'#{tc} {answer}')