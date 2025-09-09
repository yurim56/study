T = int(input())

for tc in range(1, T+1):
    txt = input()

    top = -1
    stack = [0] * 100

    ans = 1

    for x in txt:
        if x in ('(', '{'):
            top += 1
            stack[top] = x

        elif x in (')', '}'):
            if top == -1:
                ans = 0
                break
            elif x == ')':
                if stack[top] != '(':
                    ans = 0
                    break
            elif x == '}':
                if stack[top] != '{':
                    ans = 0
                    break
            top -= 1

    if top != -1: # 검사가 다 끝났는데도 괄호가 남아있을 때
        ans = 0
    
    print(f'#{tc} {ans}')