arr = ['A', 'B', 'C']
path = []

def recur(idx):
    if idx == len(arr):
        print(*path)
        return
    
    path.append(arr[idx])
    recur(idx + 1)
    path.pop()
    
    recur(idx + 1)

recur(0)