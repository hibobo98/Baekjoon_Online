M, N = map(int,input().split())
b = [0] * M
for _ in range(N):
    i, j, k = map(int, input().split())
    for c in range(i, j+1):
        b[c-1] = k

for bb in b:
    print(bb, end =" ")
