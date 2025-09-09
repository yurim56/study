# def pre_order(T):
#     if T:
#         print(T)
#         pre_order(left[T])
#         pre_order(right[T])


# N = int(input())

# arr = list(map(int, input().split()))

# left = [0]*(N+1)
# right = [0]*(N+1)
# par = [0]*(N+1)

# for i in range(N-1):
#     p, c = arr[i*2], arr[i*2+1]
#     par[c] = p

#     if left[p] == 0:
#         left[p] = c
#     else:
#         right[p] = c

# print(left)
# print(right)

# root = 1
# for i in range(1, N+1):
#     if par[i] == 0:
#         root = i
#         break

# pre_order(root)

# T = 10

# for tc in range(1, T+1):
#     N = int(input())

#     word = [0]*(N+1)
#     left_node = [0]*(N+1)
#     right_node = [0]*(N+1)

#     for i in range(1,N+1):
#         arr = input().split()
#         node_num = int(arr[0])
#         node_word = arr[1]

#         word[node_num] = node_word

#         if len(arr) > 2:
#             left_node[node_num] = int(arr[2])
        
#         if len(arr) > 3:
#             right_node[node_num] = int(arr[3])
    
#     root = 1

# def in_order(T):
#     if T:
#         in_order(left_node[T])
#         print(f'#{tc} {word[T]}', end='')
#         in_order(right_node[T])

# in_order(root)

T = 10

def inorder(node):
    if node*2 <= N: # left가 있을 때만 출력해라
        inorder(node*2)
    print(chars[tree[node]], end='')

    if node*2+1 <= N:
        inorder(node*2+1)
    

for tc in range(1, T+1):
    N = int(input())

    tree = [0]*(N+1) # 0~N번까지 인덱스를 사용하고 싶어서 -> 0번은 사용 X
    chars = ['']*(N+1)

    tree[1] = 1 # root = 1
    for i in range(N): # N개 입력
        info = input().split()
        

        if len(info) == 4:
            index, char, left, right = info
            # 2. 왼쪽 자식노드 번호 등록해놓기
            tree[int(index)*2] = left
            # 3. 오른쪽 자식노드 번호 등록해놓기
            tree[int(index)*2+1] = right

        elif len(info) == 3:
            index, char, left = info
            # 2. 왼쪽 자식노드 번호 등록해놓기
            tree[int(index)*2] = left
        
        else:
            index, char = info

        chars[int(index)] = char  # 1. 자기 인덱스에 글씨 적어넣기 -> if, elif, else에 다 들어가서 한 번에 하기

    print(f'#{tc} ', end='')
    inorder(1) # 출발지는 1임
    print()