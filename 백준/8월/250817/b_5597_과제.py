students = [0]*31

for i in range(28):
    N = int(input())
    students[N] = 1

for j in range(1, 31):
    if students[j] == 0:
        print(j)