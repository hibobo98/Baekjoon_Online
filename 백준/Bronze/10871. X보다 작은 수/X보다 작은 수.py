N, X = map(int, input().split())

A = map(int, input().split())

l = []

for i in A:
    if i < X:
        l.append(i)

for i in l:
    print(i, end=' ')