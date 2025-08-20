K, Q, R, B, N, P = 1, 1, 2, 2, 2, 8

k, q, r, b, n, p = list(map(int, input().split()))

answer = []
answer.append(K-k)
answer.append(Q-q)
answer.append(R-r)
answer.append(B-b)
answer.append(N-n)
answer.append(P-p)

print(*answer)