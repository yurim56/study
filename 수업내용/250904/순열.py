path = []
# used = [False, False, False, False, False, False, False]
used = [False]*7

def recur(count):
    if count == 3:
        print(*path)
        return
    
    for num in range(1, 7):
        if used[num]:
            continue
        
        used[num] = 1
        path.append(num)
        recur(count+1)
        path.pop()
        used[num] = 0

recur(0)