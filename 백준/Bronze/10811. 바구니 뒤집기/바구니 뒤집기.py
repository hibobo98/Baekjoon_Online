M, N = map(int,input().split())
b = [i+1 for i in range(M)]
for _ in range(N):
    i, j = map(int, input().split())
    temp = b[i-1:j]
    temp.reverse()
    b[i-1:j] = temp

for bb in b:
    print(bb, end=' ')