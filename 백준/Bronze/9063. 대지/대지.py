n = int(input())

lx = []
ly = []

for i in range(n):
    x, y = map(int, input().split())
    lx.append(x)
    ly.append(y)
if n < 2:
    print(0)
else:
    X = max(lx) - min(lx)
    Y = max(ly) - min(ly)
    print(X*Y)