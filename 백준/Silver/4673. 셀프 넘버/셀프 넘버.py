l = []
m = []
i = 0
while i <= 10000:
    a = len(str(i))
    n = str(i)
    
    if a == 1:
        s = i+i
        l.append(s)
    
    elif a == 2:
        s = int(n[0])+int(n[1])+int(n)
        l.append(s)
        
    elif a == 3:
        s = int(n[0])+ int(n[1])+int(n[2])+int(n)
        if s <= 10000:
            l.append(s)
    elif a == 4:
        s = int(n[0])+ int(n[1])+int(n[2])+ int(n[3])+int(n)
        if s <= 10000:
            l.append(s)
        
    i += 1  
l = set(l)
for j in range(10000+1):
    if j not in l:
        print(j)