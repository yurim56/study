N = int(input())

for i in range(N):
    spaces = N -1 -i
    stars = 2 * i + 1

    print(' '*spaces + '*'*stars)

for i in range(N-2, -1, -1):
    spaces = N -1 -i
    stars = 2 * i + 1
    print(' '*spaces + '*'*stars)