N = int(input())
score = 0
cnt = 1
for _ in range(N):
    ox = input()
    length = len(ox)

    for i in range(length):
        if ox[i] == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)
    score = 0
    cnt=1