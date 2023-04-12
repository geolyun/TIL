l1 = []
l2 = []

a, b, c, d, e, f = map(int, input().split())

l1.extend([a,b,c])
l2.extend([d,e,f])

if l1[0] == l2[0]:
    y = b-e
    r = c-f
    Y = int(r / y)
    X = int((f - (Y*e)) / d)
else:
    for i in range(len(l1)):
        l1[i] *= d
    for i in range(len(l2)):
        l2[i] *= a
    y = l1[1] - l2[1]
    r = l1[2] - l2[2]
    Y = int(r / y)
    X = int((f - (Y*e)) / d) 

print(X, Y)