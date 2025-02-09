# 문제 2. 19942 다이어트 

def recur(idx, dan, ji, tan, bi, price):
    global answer 
    global used
    global answer_used
    if (dan >= mp) and (ji >= mf) and (tan >= ms) and (bi >= mv):
        if answer > price:
            answer = min(answer, price)
            answer_used = []
            for i in used:
                answer_used.append(i)
    if idx == n:
        return
    
    used.append(idx+1)
    # 사용
    recur(idx+1, dan+ingred[idx][0], ji+ingred[idx][1], tan+ingred[idx][2],\
        bi+ingred[idx][3], price+ingred[idx][4])
    used.pop()
    # 미사용  
    recur(idx+1, dan, ji, tan, bi, price)


n = int(input())
mp, mf, ms, mv = map(int, input().split())
ingred = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9 
used=[]
answer_used =[]
recur(0,0,0,0,0,0)
answer_used.sort()

if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)