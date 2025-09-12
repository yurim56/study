# 1. while로 출력하기
numbers = [1,2,3,5,4,6,4,5,5,4,3,4,3]

# while len(numbers) > 0:
#     print(numbers.pop(0), end=' ')

# idx = 0

# while len(numbers) > idx:
#     print(numbers[idx], end=' ')
#     idx += 1

# 2. 재귀로 모든 요소 출력하기
def print_numbers(num):
    if num < len(numbers):
        print(numbers[num], end=' ')
        print_numbers(num+1)
    else:
        return

print_numbers(0)

