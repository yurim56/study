
def is_run(a, b, c):
    x, y, z = sorted((a, b, c))
    return (y == x + 1) and (z == y + 1)

# is_baby_gin 함수는 path에 6개가 꽉 찾을 때만 부를 것
def is_baby_gin():
    a, b, c = path[0], path[1], path[2]
    count = 0
    if a == b == c or is_run(a, b,c):
        count += 1
    
    a, b, c = path[3], path[4], path[5]
    if a == b == c or is_run(a, b, c):
        count += 1
    
    return count == 2 # 앞, 뒤 모두 만족해야하니 count == 2 면 baby gin

def recur(cnt):
    global baby_gin_result
    if baby_gin_result:
        return 
    
    if cnt == 6:
        if is_baby_gin():
            baby_gin_result =True
        return

    for i in range(len(numbers)):
        if used[i]:
            continue
        used[i] = 1
        path.append(numbers[i])
        recur(cnt + 1)
        path.pop()
        used[i] = 0

T = int(input())
for tc in range(1, T+1):
    s = input().strip()
    # 공백이 있으면 split, 없으면 글자별 파싱
    if ' ' in s:
        numbers = list(map(int, s.split()))
    else:
        numbers = [int(ch) for ch in s]

    # (안전장치) 길이 6이 아니면 false
    if len(numbers) != 6:
        print(f"#{tc} false")
        continue

    path = []
    used = [0]*len(numbers)
    baby_gin_result = False
    
    recur(0)
    print(f"#{tc} {'true' if baby_gin_result else 'false'}")
