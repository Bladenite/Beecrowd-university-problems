while True:
    X1, Y1, X2, Y2 = map(int, input().split())
    if X1 == 0:
        break
    elif X1 == X2 and Y1 == Y2:
        resultado = 0
    elif X1 == X2 or Y1 == Y2:
        resultado = 1
    elif abs(X2 - X1) == abs(Y2 - Y1):
        resultado = 1
    else:
        resultado = 2
    print(resultado)
