# 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 것
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

path = []

def subset(count):
    if count == len(arr):
        if path and sum(path) == 0:
            print(set(path))
        return
    
    path.append(arr[count])
    subset(count + 1)
    path.pop()
    subset(count + 1)

subset(0)