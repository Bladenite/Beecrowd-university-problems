contador = 0
while True:
    N = int(input()) 
    if N == 0:
        break
    listaDeChegada = list(map(int, input().split()))
    contador += 1
    print("Teste", contador)
    for i in range(N):
        if listaDeChegada[i] == i + 1:
                print(i + 1)
    print()