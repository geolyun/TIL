n, m = map(int, input().split())

a = []

for i in range(1, n+1):
    a.append(i)

for i in range(m):
    i, j = map(int, input().split())
    
    a[i-1:j] = reversed(a[i-1:j])

print(*a)