n, m = map(int, input().split())

l = []

for a in range(1, n+1):
    l.append(a)

for _ in range(m):
    i, j, k = map(int, input().split())
    rev = l[i-1:j]
    for b in range(k-i):
        rev.append(rev.pop(0))
    l[i-1:j] = rev
    

print(*l)