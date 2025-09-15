# 이 중 최소 2명 이상의 친구와 함께 카페에 갈 것
# 몇 가지 경우가 가능??
friends = ['A', 'B', 'C', 'D', 'E']
n = len(friends)

path = []
count = 0 # 경우의 수

def subset(idx):
    global count

    if idx == n:
        if len(path) >= 2:
            print(path)
            count += 1
        return
    
    path.append(friends[idx])
    subset(idx + 1)
    path.pop()
    subset(idx + 1)

subset(0)
print('경우의 수:', count)

