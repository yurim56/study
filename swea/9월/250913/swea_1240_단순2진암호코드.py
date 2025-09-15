T = int(input())

orders = {
    0:'0001101', 1:'0011001', 2:'0010011',
    3:'0111101', 4:'0100011', 5:'0110001',
    6:'0101111', 7:'0111011', 8:'0110111', 9:'0001011'
         }

for tc in range(1, T+1):
    N, M = map(int, input().split())
    password = [input() for _ in range(N)]
    
    target = ''
    for line in password:
        if '1' in line:
            target = line
    
    for order in orders:
        if orders[order] in target:
            print(orders[order])