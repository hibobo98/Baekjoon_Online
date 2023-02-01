N = int(input()) 
score = list(map(int, input().split()))
M = max(score)
l = []
for i in score:
    new_score = i/M*100
    l.append(new_score)
print(sum(l)/N)