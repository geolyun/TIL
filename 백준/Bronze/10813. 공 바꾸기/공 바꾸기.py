n, m = map(int, input().split())

l = []

for a in range(1, n+1):
    l.append(a)

for a in range(m):
    i, j = map(int, input().split())
    l[i-1], l[j-1] = l[j-1], l[i-1]

print(*l)