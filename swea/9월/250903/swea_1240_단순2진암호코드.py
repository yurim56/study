code_map = {
    '0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
    '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9
}

T = int(input().strip())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    target = ""
    for _ in range(N):
        s = input().strip()
        if '1' in s:
            target = s

    end = target.rfind('1')
    start = end - 55
    if end == -1 or start < 0:
        print(f"#{tc} 0")
        continue

    bits = target[start:end+1]
    digits = []
    ok = True
    for i in range(0, 56, 7):
        seg = bits[i:i+7]
        if seg in code_map:
            digits.append(code_map[seg])
        else:
            ok = False
            break

    if ok and len(digits) == 8:
        chk = sum(digits[0:7:2]) * 3 + sum(digits[1:7:2]) + digits[7]
        ans = sum(digits) if chk % 10 == 0 else 0
    else:
        ans = 0

    print(f"#{tc} {ans}")
