import sys

arr = [int(input()) for _ in range(9)]
pick = []

def comb(count, idx):
    if count == 7:
        if sum(pick) == 100:
            for i in sorted(pick):
                print(i) 
            exit()
        return
    
    for i in range(idx, len(arr)):
        pick.append(arr[i])
        comb(count + 1, i + 1)
        pick.pop()

comb(0, 0)