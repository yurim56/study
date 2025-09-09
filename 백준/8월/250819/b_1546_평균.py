# N = int(input())
# scores = list(map(int, input().split()))

# max_score = max(scores)

# new_score = []
# for i in scores:
#     new_score.append(i/max_score*100)
# average = sum(new_score) / N
# print(average)


N = int(input()) 
scores = list(map(int, input().split())) 

max_socre = max(scores) 

else_score = [] 
for score in scores: 
    if score != max_socre: 
        else_score.append(score) 
print(else_score) 

new_score = [] 
for i in else_score: 
    new_score.append(i/max_socre*100) 
new_score.append(max_socre/max_socre*100) 

print(new_score) 

print(sum(new_score)/N)