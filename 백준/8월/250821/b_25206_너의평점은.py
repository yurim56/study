creditss = {
    'A+':4.5, 'A0':4.0,
    'B+':3.5, 'B0':3.0,
    'C+':2.5, 'C0':2.0,
    'D+':1.5, 'D0':1.0,
    'F':0.0
}
total_credits = 0
total_score = 0

for _ in range(20):
    subject, credits, grade = input().split()
    if grade == 'P':
           continue
    
    credits = float(credits)
    total_credits += credits
    total_score += credits*creditss[grade]

if total_credits == 0:
      final_score = 0
else:
      final_score = total_score / total_credits

print(final_score)