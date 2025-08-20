# import string

# word = input()
# if word in list(string.ascii_letters):

word = input().upper()

# 효율적으로 알파벳 개수 세기
num = {}
for i in word:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1

# 이 아래 부분은 원래 코드와 동일하며, 효율성에 문제가 없습니다.
count = list(num.values())

# 딕셔너리가 비어있는 경우(입력이 없을 때)를 대비
if not count:
    print("?")
else:
    max_count = max(count)

    if count.count(max_count) != 1:
        print('?')
    else:
        for i, c in num.items():
            if c == max_count:
                print(i)
                break