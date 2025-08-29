def in_order(node, a):
    if node > N:
        return 0
    l = in_order(node*2, a)
    tree[node] = l + a + 1
    r = in_order(node*2+1, tree[node])
    return l + r + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)

    in_order(1, 0)

    print(f'#{tc} {tree[1]} {tree[N//2]}')



def in_order(node):
    global count

    if node > N:
        return
    
    in_order(node*2)
    tree[node] = count
    count += 1
    in_order(node*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)

    count = 1

    in_order(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')