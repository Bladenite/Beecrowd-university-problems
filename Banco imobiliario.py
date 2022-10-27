I, N = map(int, input().split())

D = E = F = I

matriz = []

for i in range(0, N):
    lista = []
    lista = input().split()
    matriz.append(lista)
for i in range(0, N):
    if len(matriz[i]) == 4:
        if matriz[i][1] == "D":
            D += int(matriz[i][3])
        if matriz[i][1] == "E":
            E += int(matriz[i][3])
        if matriz[i][1] == "F":
            F += int(matriz[i][3])
        if matriz[i][2] == "D":
            D -= int(matriz[i][3])
        if matriz[i][2] == "E":
            E -= int(matriz[i][3])
        if matriz[i][2] == "F":
            F -= int(matriz[i][3])
    if matriz[i][0] == "V": 
        if matriz[i][1] == "D":
            D += int(matriz[i][2])
        elif matriz[i][1] == "E":
            E += int(matriz[i][2])
        elif matriz[i][1] == "F":
            F += int(matriz[i][2])

    if matriz[i][0] == "C":
        if matriz[i][1] == "D":
            D -= int(matriz[i][2])
        elif matriz[i][1] == "E":
            E -= int(matriz[i][2])
        elif matriz[i][1] == "F":
            F -= int(matriz[i][2])
            

print(D, E, F)