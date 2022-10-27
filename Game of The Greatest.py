N = -1
A_ScoreList = []
B_ScoreList = []

while N != 0:   
    A = 20
    B = 20
    N = -1
    Ascore = 0
    Bscore = 0

    while N < 0 or N > 10:
        N = int(input())

    for i in range(N):
        while (A and B <= 0) or (A and B > 10):
            A, B = input().split()
            A = int(A)
            B = int(B)
        if A > B:
            Ascore += 1
        elif B > A:
            Bscore += 1
        A, B = 20, 20
    A_ScoreList.append(Ascore)
    B_ScoreList.append(Bscore)

for i in range(len(A_ScoreList) - 1):
    print(A_ScoreList[i], B_ScoreList[i])

