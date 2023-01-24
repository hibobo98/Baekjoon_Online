N, X = map(int, input().split())

A = map(int, input().split())

l = []

for i in A:
    if i < X:
        print(i, end= ' ')