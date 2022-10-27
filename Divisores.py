A, B, C, D = map(int, input().split())
n = -1
if A != B and C != D:
    inicio = A
    fim = C
    while fim > inicio: 
        if inicio % A == 0 and inicio % B != 0 and C % inicio == 0 and D % inicio != 0:
            n = inicio
            break
        inicio += A

print(n)
