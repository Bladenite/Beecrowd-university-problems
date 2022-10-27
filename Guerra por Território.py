N = int(input())
a = [int(x) for x in input().split()]

soma = sum(a)
soma_adicional = 0

for i in range(N):
    soma_adicional += a[i]
    if soma_adicional == (soma/2):
        print(i+1)
        break

