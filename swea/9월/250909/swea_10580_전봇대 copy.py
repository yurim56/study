T = int(input())

for tc in range(1, T+1):
    N = int(input())
    wires = []
    
    for i in range(N):
        A, B = map(int, input().split())
        wires.append((A,B))    
    
        # if 