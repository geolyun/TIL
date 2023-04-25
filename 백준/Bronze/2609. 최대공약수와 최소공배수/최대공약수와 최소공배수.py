a, b = map(int, input().split())

m = min(a,b)
p = 0
q = 0

for i in range(1, m+1):
    if a % i == 0 and b % i == 0:
        p = i

q = (a // p) * (b // p) * p

print(p)
print(q)