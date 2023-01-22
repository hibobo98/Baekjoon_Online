import sys

N = sys.stdin.readline().rstrip()
tot = sys.stdin.readline().rstrip().split()
v = sys.stdin.readline().rstrip()

l = []

for i in tot:
    if i == v:
        l.append(i)

print(len(l))
