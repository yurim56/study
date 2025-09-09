N = int(input())

# def fact(n):
#     if n <= 1:
#         return 1
#     answer =  n * fact(n-1)
#     return answer

# print(fact(N))

# def fact(n):
#     if n <= 0:
#         answer = 1
#         return answer
#     answer =  n * fact(n-1)
#     if n==N:
#         print(answer)
#     return answer

# fact(N)

def fact(n):
    if n <= 1:
        if N <= 1:
            print(1)
        return 1
    
    answer =  n * fact(n-1)

    if n==N:
        print(answer)
    return answer

fact(N)

# 1. while로 출력하기
# 2. 재귀로 모든 요소 출력하기
numbers = [1,2,3,5,4,6,4,5,5,4,3,4,3]


# ans = []

# def fact(n):
#     if n <= 1:
#         return 1
#     answer =  n * fact(n-1)
#     ans.append(answer)
    
#     return answer

# fact(N)
# print(ans[-1])