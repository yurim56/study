arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []

def recur(count, start):
    if count == N:
        print(*path)
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(count + 1, i + 1)
        path.pop()

recur(0, 0)