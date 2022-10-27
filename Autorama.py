K, N, M = map(int, input().split())
matriz = []
pontos = [0, 0, 0]

for i in range(M):
    lista = []
    carrinho, posto = map(int, input().split())
    lista.append(carrinho)
    lista.append(posto)
    matriz.append(lista)
