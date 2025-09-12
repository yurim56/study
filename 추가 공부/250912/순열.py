numbers = [0, 1, 2]
pick_number = []
visited = [0] * len(numbers)

M = 2

def perm(count):
    if count == M:
        print(*pick_number)
        return
    
    for i in range(len(numbers)):
        if visited[i] == 1:
            continue
        visited[i] = 1
        pick_number.append(numbers[i])
        perm(count + 1)
        pick_number.pop()
        visited[i] = 0    

perm(0)
