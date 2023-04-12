l = []

a, b, c = map(int, input().split())
l.append(a)
l.append(b)
l.append(c)

l.sort(reverse=True)

if l[0] >= l[1] + l[2]:
    l[0] = l[1] + l[2] - 1
    print(l[0]+l[1]+l[2])
else:
    print(l[0]+l[1]+l[2])