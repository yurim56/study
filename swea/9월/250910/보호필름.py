'''
한 층에 대해 아무것도 안할 수도, A를 넣을 수도, B를 넣을 수도
모든 층에 대해 모든 케이스를 다 봐줘야 함.
'''

def test_films(films):
    for c in range(W): # 열 우선 순회
        count = 0
        before = -1
        test_pass = False
        for r in range(D):
            if films[r][c] == before:
                count += 1
            else:
                count = 1
                before = films[r][c]
              
            if count >= K: # 연속으로 K개 이상 같은 값이면 그 열 통과
                test_pass = True
                break
        if not test_pass: # 하나라도 실패한 경우 검사 실패
            return False
    return True
  
def dfs(films, count, idx):
    global answer
  
    if test_films(films):
        answer = min(answer, count)
  
    if answer <= count:
        return
  
    if count == K-1: # K-1개 이상 바꾸면 의미 없음 -> 최대 K-1개만 고려
        return
      
    next_films = films[:]
    for i in range(idx, D): 
        next_films[i] = A
        dfs(next_films, count+1, i+1)
        next_films[i] = B
        dfs(next_films, count+1, i+1)
        next_films[i] = films[i]
          
              
              
T = int(input())
  
A = (0,)*20
B = (1,)*20
  
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
  
    answer = K # 최악의 경우 : K개 층을 바꿔야 함
  
    dfs(films, 0, 0)
  
    print(f'#{tc} {answer}')