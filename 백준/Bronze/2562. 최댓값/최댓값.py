l = []
for _ in range(9):
    N = int(input())
    l.append(N)

print(max(l))

print(l.index(max(l))+1)