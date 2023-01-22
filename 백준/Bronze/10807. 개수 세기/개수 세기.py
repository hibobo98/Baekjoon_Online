N = int(input())
tot = map(int, input().split())
v = int(input())
l = []

for i in tot:
    if i == v:
        l.append(i)

print(len(l))