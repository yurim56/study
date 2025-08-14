T = 10

stack = [0] * 100

for tc in range(1, T+1):
    lst_len = int(input())
    infix = input()
    top = -1
    postfix = '' # 후위식

    for token in infix:
        if token != '+': # 피연산자면 후위식에 추가
            postfix += token
            while top > -1:
                top -= 1
                postfix += stack[top+1]

        else: # 연산자인 경우 비어있거나 
            top += 1 # push
            stack[top] = token
        

    for i in postfix:
        if i != '+':
            top += 1
            stack[top] = int(i)
        else:
            out2 = stack[top]
            top -= 1
            out1 = stack[top]
            top -= 1
            if i == '+':
                top += 1
                stack[top] = out1 + out2
    print(f'#{tc} {stack[top]}')
            
# for tc in range(1, 2):
#     N = int(input())
#     lst = list(input())
#     bin_list = []
#     for i in range(N):
#         if i % 2 == 0:
#             bin_list.append(int(lst[i]))
#     print(sum(bin_list))