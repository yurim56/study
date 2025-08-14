stack = [0] * 100
top = -1

icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 밖에 있을 때의 우선 순위(클수록 높음)
isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택 안에서의 우선 순위(클수록 높음)

infix = '(6+5*(2-8)/2)'
postfix = '' # 후위식

for token in infix:
    if token not in '(+-*/)': # 피연산자면 후위식에 추가
        postfix += token
    elif token == ')': # 닫는 괄호면 여는 괄호를 만날 때까지 pop
        while top > -1 and stack[top] != '(':
            top -= 1
            postfix += stack[top+1]
        if top != -1: # 전체 수식이 괄호로 둘러 쌓이지 않은 경우
            top -= 1 # '(' 버림

    else: # 연산자인 경우 비어있거나 
        if top == -1 or isp[stack[top]] < icp[token]: # 토큰의 우선순위가 더 높으면
            top += 1 # push
            stack[top] = token
        elif isp[stack[top]] >= icp[token]: # 토큰과 같거나 더 높으면
            while top > -1 and isp[stack[top]] >= icp[token]:
                postfix += stack[top]
                top -= 1
            top += 1 # push
            stack[top] = token
    print(postfix)