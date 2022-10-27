N = int(input())
matriz= []

for i in range(N):
    lista = []
    A , B = map(int, input().split())
    lista.append(A)
    lista.append(B)
    matriz.append(lista)

for i in range(N):
    numero = str(matriz[i][0])
    numero_comparado = str(matriz[i][1])
    sl = len(numero) - len(numero_comparado)
    if numero[sl:] == numero_comparado:
        print("encaixa")
    else:
        print("nao encaixa")

   


