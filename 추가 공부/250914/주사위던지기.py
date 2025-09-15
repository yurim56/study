# 주사위 N개를 던져서 나올 수 있는 눈금의 모든 조합

dice = [1, 2, 3, 4, 5, 6]
n = 3
path = []

def recur(count, start):
    if count == n:
        print(path)
        return
    
    for i in range(start, len(dice)):
        path.append(dice[i])
        recur(count + 1, i)
        path.pop()

recur(0, 0)