# 주사위 3개를 던져서 합이 10 이하인 케이스의 수

path = [] # 무조건 기존 주사위를 기록해놔야 할까..?
result = 0

# def recur(count):
#     global result
    
#     # 이미 10을 넘은 경우는 더 볼 필요가 없다
#     # 기저 조건에서 많은 경우의 수를 줄일 수 있다
#     if sum(path) > 10:
#         return
    
#     if count == 3:
#         if sum(path) <= 10:
#             print(*path)
#             result += 1
            
#         return
    
#     for num in range(1, 7):
#         path.append(num)
#         recur(count + 1)
#         path.pop()

# recur(0)

# 누적합을 활용하는 버전-----------------------------
def recur(count, total):
    global result
    
    if total > 10:
        return
    
    if count == 3:
        if total <= 10:
            print(*path)
            result += 1
            
        return
    
    for num in range(1, 7):
        recur(count + 1, total + num)
        
recur(0, 0)