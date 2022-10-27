T = int(input())
for i in range(T):
    n = int(input())
    p = []
    for r in range(n):
        e = str(input()).split()
        if e[0] == 'LEFT': 
            p.append(-1)
        elif e[0] == 'RIGHT': 
            p.append(1)
        else: p.append(p[int(e[2]) - 1])
    print(sum(p))




        
