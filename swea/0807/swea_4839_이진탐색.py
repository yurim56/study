# 이진 탐색 함수
def binarySearch(N, key):
    start = 1
    end = N
    count = 0
    while start <= end:
        count += 1
        middle = (start+end)//2
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else:
            start = middle
    return count

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    
    a_find = binarySearch(P, A)
    b_find = binarySearch(P, B)

    if a_find < b_find:
        print(f'#{tc} A')
    elif a_find == b_find:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')
