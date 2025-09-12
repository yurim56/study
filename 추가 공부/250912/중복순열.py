path = []

def recur(count):
    if count == 2:
        print(*path)
        return
    
    for i in range(1, 7):
        path.append(i)
        recur(count + 1)
        path.pop()

recur(0)