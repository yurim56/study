arr = ['A', 'B', 'C']
n = len(arr)

# for i in range(1 << n):
#     subset = []
#     for j in range(n):
#         if i & (1 << j):
#             subset.append(arr[j])
#     print(subset)

def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1

for tar in range(1 << n):
    print('{', end='')
    get_sub(tar)
    print('}')