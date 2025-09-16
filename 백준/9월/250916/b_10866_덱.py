import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
que = deque()

for _ in range(N):
    order = list(input().split())
    
    if len(order) == 2:
        if order[0] == 'push_front':
            que.appendleft(order[1])

        elif order[0] == 'push_back':
            que.append(order[1])
    
    else:
        if order[0] == 'pop_front':
            if que:
                print(que.popleft())
            else:
                print(-1)
        
        elif order[0] == 'pop_back':
            if que:
                print(que.pop())
            else:
                print(-1)
        
        elif order[0] == 'size':
            print(len(que))
        
        elif order[0] == 'empty':
            if que:
                print(0)
            else:
                print(1)
        
        elif order[0] == 'front':
            if que:
                print(que[0])
            else:
                print(-1)                
        
        elif order[0] == 'back':
            if que:
                print(que[-1])
            else:
                print(-1)