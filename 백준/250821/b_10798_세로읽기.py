arr = [list(input()) for _ in range(5)]

max_len = 0
for word in arr:
    if len(word) > max_len:
        max_len = len(word)

# result = ''
for r in range(max_len):
    for c in range(5):
        if r < len(arr[c]):
            print(arr[c][r], end='')
