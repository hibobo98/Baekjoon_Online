N = int(input())

n = N // 4 
if N % 4 > 0 : 
    n += 1
print("long "*n,"int", sep="")