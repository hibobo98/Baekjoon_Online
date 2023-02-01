l = []
for i in range(28):
    N = int(input())
    l.append(N)

check  =[]
for i in range(1,31):
    if i not in l:
        check.append(i)

print(min(check))
print(max(check))