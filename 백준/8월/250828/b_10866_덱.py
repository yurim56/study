from collections import deque

que = deque()

N = int(input())

for _ in range(N):
    order = input().split()

    if order[0] == 'push_front':
        if order[1]:
            que.appendleft(order[1])

    elif order[0] == 'push_back':
        if order[1]:
            que.append(order[1])

    elif order[0] == 'pop_front':
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