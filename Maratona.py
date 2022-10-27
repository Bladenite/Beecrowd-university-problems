N, M = input().split()
N, M = int(N), int(M)
P = list(map(int, input().split()))

df = 42195

for i in range(len(P) - 1, -1, -1):
    temp = df - P[i]
    if temp <= M:
        df = P[i]
    else:
        print("N")
        exit()
print("S")
    
