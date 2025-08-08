numbers = [1, 2, 3, 4, 5]
picked_numbers = []
M = 3

def comb(count, idx): # 내가 고른 인덱스 : idx
    print(picked_numbers)
    if count == M:
        return
    
    for i in range(idx, len(numbers)):
        picked_numbers.append(numbers[i])
        comb(count+1, i+1) # 전달해줄 값은 i이기에 idx가 오는 것이 아님
        picked_numbers.pop()

comb(0, 0)


numbers = [1, 2, 3, 4, 5]
picked_numbers = []
M = 3

def comb(count, idx): # 내가 고른 인덱스 : idx
    if count == M:
        print(picked_numbers)
        return
    
    for i in range(idx, len(numbers)):
        picked_numbers.append(numbers[i])
        comb(count+1, i+1) # 전달해줄 값은 i이기에 idx가 오는 것이 아님
        picked_numbers.pop()

comb(0, 0)
    
    