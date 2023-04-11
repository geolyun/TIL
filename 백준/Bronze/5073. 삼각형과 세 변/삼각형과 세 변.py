res = []

while True:
    l = []
    a, b, c = map(int, input().split())
    l.append(a)
    l.append(b)
    l.append(c)
    l.sort(reverse=True)
    if a == 0 and b == 0 and c == 0:
        break
    if l[0] >= l[1] + l[2]:
        res.append("Invalid")
    else:
        if a == b == c:
            res.append("Equilateral")
        elif a == b or b == c or a == c:
            res.append("Isosceles")
        else:
            res.append("Scalene")

for i in res:
    print(i)