a = {}

for i in range(10):
    b = int(input())
    a[b%42] = i
print(len(a))