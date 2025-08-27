import sys

input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    command = input().split()
    order = int(command[0])

    if order == 1:
        stack.append(int(command[1]))

    elif order == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif order == 3:
        print(len(stack))
    
    elif order == 4:
        if stack:
            print(0)
        else:
            print(1)

    elif order == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)