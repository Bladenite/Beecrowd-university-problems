N = int(input())
esforço = []


for i in range(N):
    trilha = [int(i) for i in input().split()]
    soma = 0
    soma_inversa = 0
    for j in range(1, len(trilha) - 1):
        if trilha[j+1] > trilha[j]:
            soma += trilha[j+1] - trilha[j]
        elif trilha[j+1] < trilha[j]:
            soma_inversa += trilha[j] - trilha[j+1]
    if soma > soma_inversa:
        esforço.append(soma_inversa)
    else:
        esforço.append(soma)

menor_trilha = esforço.index(min(esforço))
print(menor_trilha+1)




