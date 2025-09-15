# 완전 탐색으로 부분 집합 구하기
# {MIN, CO, TIM} -> 함께 영화관에 갈 때 나오는 모든 경우의 수

arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']

def run(level):
    if level == 3:
        print(*path)
        return

    for i in range(2):
        path.append(arr[i])
        run(level + 1)
        path.pop()

run(0)