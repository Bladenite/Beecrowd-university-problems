#proteja sua senha

from binascii import a2b_base64


contador = 0
while True:
    N = input()
    if N == 0:
        break


    colunas = []
    linhas= []


    for i in range(N):
        lista = input().split()

    for i in range(10):
        for j in range(2):
            linhas.append(lista[j]) 
        



        