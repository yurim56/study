N = int(input())


if N == 0:
    print(0)

else:
    num = []
    while N > 0:
        num.append(N % 2)
        N //= 2

    num.reverse()

    print(''.join(map(str, num)))