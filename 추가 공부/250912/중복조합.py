arr = ['A', 'B', 'C', 'D', 'E']
path = []

def recur(count, start):
    if count == 3:
        print(*path)
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(count + 1, i)
        path.pop()

recur(0, 0)