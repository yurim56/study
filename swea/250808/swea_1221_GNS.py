T = int(input())

alp = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
]


for tc in range(1, T+1):
    t_case, length = input().split()
    input_alp = input().split()

    new = []

    for i in alp:
        for j in input_alp:
            if i == j:
                new.append(j)
    print(f'#{tc}')
    print(' '.join(new))