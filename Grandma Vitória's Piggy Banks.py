contador = 1
while True:
    dif = 0
    listaj = []
    listaz = []
    N = int(input())
    if N == 0:
        break
    for i in range(N):
        J, Z = input().split()
        J, Z = int(J), int(Z)
        listaj.append(J)
        listaz.append(Z)

    print("Teste", contador)
    contador += 1
    for i in range(N):
        dif = listaj[i] - listaz[i] + dif
        print(dif)
    print()