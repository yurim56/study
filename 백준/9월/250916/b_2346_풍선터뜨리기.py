from collections import deque

N = int(input())
nums = list(map(int, input().split()))
ballons = deque((i+1, nums[i]) for i in range(N))
answer = []

while ballons:
    idx, move = ballons.popleft()
    answer.append(idx)
    
    if not ballons:
        break
    
    if move > 0:
        for _ in range(move-1):
            ballons.append(ballons.popleft())
    
    else:
        for _ in range(-move):
            ballons.appendleft(ballons.pop())

print(*answer)