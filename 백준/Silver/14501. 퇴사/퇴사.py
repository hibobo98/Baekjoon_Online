def recur(idx, result):
    global answer

    # 퇴사 후 (상담을 더 이상 할 수 없는 상태)
    if idx >= n:
        answer = max(answer, result)
        return
    
    # 상담을 진행하는 경우 (idx + table[idx][0]일 후에 퇴사)
    if idx + table[idx][0] <= n:
        recur(idx + table[idx][0], result + table[idx][1])

    # 상담을 진행하지 않는 경우 (다음 날로 넘어감)
    recur(idx + 1, result)
    
n = int(input())  # 퇴사까지의 날짜 수
table = [[] for _ in range(n+1)]  # table[0]부터 사용할 수 있도록 크기 설정

# 상담 정보 입력
for i in range(n):
    a, b = map(int, input().split())
    table[i] = [a, b]  # table[0]부터 사용

answer = 0 
recur(0, 0)  # 0일부터 시작
print(answer)
