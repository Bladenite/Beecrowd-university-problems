while True:
    try:
        A, B, C = input().split()
        A, B, C = int(A), int(B), int(C)
    except EOFError:
        break
    if A != B and A != C:
        print("A")
    elif B != A and B != C:
        print("B")
    elif C != A and C != B:
        print("C")
    else:
        print("*")
    