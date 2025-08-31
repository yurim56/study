numbers = [1, 2, 3, 4, 5]
picked_numbers = []
M = 3
visited = [0]*len(numbers)

def perm(count):
    if count == M:
        print(picked_numbers)
        return
    
    for i in range(len(numbers)):
        if visited[i] == 1:
            continue
        picked_numbers.append(numbers[i])
        visited[i] = 1
        perm(count+1)
        picked_numbers.pop()
        visited[i] = 0

perm(0)
    