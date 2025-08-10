# 1번째 풀이
# T = int(input())

# for tc in range(1, T+1):
#     k, n, m = list(map(int, input().split()))
#     stop = list(map(int, input().split()))

#     for i in range(1, n+1):
#         # 연료 소진
#         k -= 1

#         # 도달 불가능한 지점인 경우
#         if k < 0:
#             charge = 0
#             break

#         # 충전소가 없는 정류장일 경우
#         if i not in stop:
#             continue

#         # 종점과 다음 충전소에 못 갈 때 충전하기
#         if i+k < n and (stop.index(i) == len(stop)-1 or i+k < stop[[stop.index(i)+1]]):
#             k = init_k
#             charge += 1

#     print(f'#{tc} {charge}')

# 2번째 풀이
# while 문 사용 -> 종료 조건 : 종점에 도착할 때까지
T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    station = list(map(int, input().split()))
    station.append(n)
 
    position = 0
    count = 0
    while position + k < n:
     
        reachable = [i for i in station if position< i < position+k+1]
        if not reachable:
            count = 0
            break          
        position = max(reachable)
        count += 1
 
    print(f"#{tc} {count}")