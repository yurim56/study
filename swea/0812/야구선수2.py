T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    stats = list(map(int, input().split())) # 실력
    
    answer = 1 # 팀원이 1명인 경우는 없음

    # 2명 이상 팀일 경우 생각하기
    stats.sort() # sorted(stats) -> 얘는 정렬 값을 새로 저장해준다는 것

    left = 0
    right = 0

    # 끝나는 규칙이 정확하지 않아서 while문 사용
    while right < N:

        if stats[right] - stats[left] <= K:
            right += 1
            answer = max(answer, right-left+1)
            continue

        left += 1

    print(answer)
