N = int(input())
coord_x = []
coord_y = []

for i in range(N):
    X, Y = map(int, input().split())
    coord_x.append(X)
    coord_y.append(Y)

set_x = {coord_x}
set_y = [coord_y]

if len(set_x) != len(coord_x) and len(set_y) != len(coord_y) :

print()