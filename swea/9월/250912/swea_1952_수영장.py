# # 종료 조건 : 12월을 모두 고려한 경우
# # 가지의 수 : 4개 (1일, 1달, 3달, 1년)

# def recur(month, total_cost):
#     global min_answer
#     if month > 12:
#         # 최소값 갱신하기
#         min_answer = min(min_answer, total_cost)
#         return

#     # 1일권으로 다 사는 경우
#     recur(month + 1, total_cost + (days[month] * cost_day))
#     # 1달권으로 다 사는 경우
#     recur(month + 1, total_cost + cost_month)
#     # 3달권으로 다 사는 경우
#     recur(month + 3, total_cost + cost_month3)
#     # 1년권으로 다 사는 경우
#     recur(month + 12, total_cost + cost_year)
    
# T = int(input())

# for tc in range(1, T+1):
#     # 이용권 가격들
#     cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
#     # 12개월 이용 계획 -> 1부터 쓴다
#     days = [0] + list(map(int, input().split()))
    
#     min_answer = 31 * 12 * 3000 # 나올 수 있는 최대 금액(31일, 12개월, 3000원 이하)
#     recur(1, 0) # 1월부터 시작
     
#     print(f'#{tc} {min_answer}')

# --------------------------------DP----------------------------------

