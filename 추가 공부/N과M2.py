numbers = [1, 2, 3, 4, 5]
N = 3
picked = []
answer = 0

# 중복 순열
def repetition_perm(count):
    global answer
    if count == N:
        print('중복 순열 :', picked)
        answer += 1
        return
    
    for i in range(len(numbers)):
        picked.append(numbers[i])
        repetition_perm(count + 1)
        picked.pop()

repetition_perm(0)
print('총 개수 :', answer)

print('========================')

# 순열
visited = [0]*len(numbers)
answer = 0
def perm(count):
    global answer
    if count == N:
        print('순열 :', picked)
        answer += 1        
        return
    
    for i in range(len(numbers)):
        if visited[i] == 0:
            picked.append(numbers[i])
            visited[i] = 1
            perm(count + 1)
            picked.pop()
            visited[i] = 0

perm(0)
print('총 개수 :', answer)

print('========================')

# 중복 조합
answer = 0
def repetition_comb(count, idx):
    if count == N:
        global answer
        answer += 1
        print('중복 조합 :', picked)
        return
    
    for i in range(idx, len(numbers)):
        picked.append(numbers[i])
        repetition_comb(count + 1, i)
        picked.pop()

repetition_comb(0, 0)
print('총 개수:', answer)

print('========================')

# 조합
answer = 0
def comb(count, idx):
    global answer
    if count == N:
       answer += 1
       print('조합 :', picked) 
       return
    
    for i in range(idx, len(numbers)):
        picked.append(numbers[i])
        comb(count+1, i+1)
        picked.pop()

comb(0, 0)
print('총 개수 :', answer)

print('========================')

# 부분 집합
answer = 0

def subset(count, idx):
    global answer
    if count >= N:
        print('부분 집합 :', picked)
        answer += 1
    
    
    for i in range(idx, len(numbers)):
        picked.append(numbers[i])
        subset(count + 1, i + 1)
        picked.pop()

subset(0, 0)
print('총 개수 :', answer)


# 부분 집합
# answer = 0

# def subset(count, idx):
#     global answer
#     print('부분 집합 :', picked)
#     answer += 1
    
#     for i in range(idx, len(numbers)):
#         picked.append(numbers[i])
#         subset(count + 1, i + 1)
#         picked.pop()

# subset(0, 0)
# print('총 개수 :', answer)