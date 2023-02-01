l = []
for _ in range(10):
    N = int(input())
    last = N % 42
    l.append(last)

l = set(l)
print(len(l))