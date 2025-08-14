# 필요 데이터

# N : 스위치 수
# switches : 스위치의 상태(입력 받기)
# M : 명령의 수
# gender : 명령의 성별
# number : 명령의 번호
# idx : 몇 배수인 지 확인
# l, r : 여자 명령을 수행하는 경우, 좌측 인덱스와 우측 인덱스

# 로직

# 1. N, switches, M 입력
# 2. M줄에 걸쳐서 명령을 입력받기 (for)
#    ㄱ. 남자일 때
#        - number부터 배수에 대하여 상태를 스왑해주기

#    ㄴ. 여자일 때
#        - 가운데 number 변경
#        - 좌우 대칭(l 지점과 r 지점이 값이 같을 때)을 만족할 때까지 반복
#          a. 해당 지점의 값을 스왑
#          b. l, r 지점을 갱신

# a = (a+1) % 4 -> 
N = int(input())
switches = list(map(int, input().split()))
switches.insert(0,0) # 인덱스 번호를 뒤로 한 칸 미루기

M = int(input())
for _ in range(M):
    gender, number = map(int, input().split()) # unpacking 할 거니까 리스트 필요 없음
    
    if gender == 1: # 남자일 때
        
        idx = 1
        while number*idx <= N: # 리스트 안 쪽에 있을 때
            switches[number*idx] = (switches[number*idx]+1)%2
            idx += 1

    else: # 여자일 때
        switches[number] = (switches[number]+1)%2
        l = number - 1
        r = number + 1 
        
        while 1 <= l and r <= N and switches[l] == switches[r]:
            switches[l] = (switches[l]+1)%2
            switches[r] = (switches[r]+1)%2
            l -= 1
            r += 1

i = 1
while i <= N:
    print(*switches[i:i+20])
    i += 20

for i in range(1, N+1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print()