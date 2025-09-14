# ['A', 'B', 'C', 'D', 'E']
# 5명 중 3명을 뽑을 수 있는 경우

arr = ['A', 'B', 'C', 'D', 'E']
n = 3
path = []
total = 0

def recur(count, start):
    global total
    if count == n:
        print(*path)
        total += 1
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(count + 1, i+1)
        path.pop()

recur(0, 0)
print(total)