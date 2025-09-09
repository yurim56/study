T = int(input())

def minHip(value):
    global last, heap
    last += 1
    heap[last] = value

    child = last
    parent = child // 2
    while parent and heap[parent] > heap[child]: # 부모가 있고, 부모 > 자식인 경우 자리 교환
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    heap = [0] * (N+1)
    last = 0

    for num in numbers:
        minHip(num)
    
    total_sum = 0
    current_idx = last

    while current_idx > 1:
        current_idx = current_idx // 2
        total_sum += heap[current_idx]

    print(f'#{tc} {total_sum}')
    