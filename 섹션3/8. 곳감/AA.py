n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    a, b, c = map(int,input().split())
    if b == 0:
        for _ in range(c):
            num[a-1].append(num[a-1].pop(0))
    else:
        for _ in range(c):
            num[a-1].insert(0, num[a-1].pop())

res = 0
s = 0
e = n-1

for i in range(n):
    for j in range(s, e+1):
        res += num[i][j]
    if i < n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(res)