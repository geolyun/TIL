n = int(input())

res = []

for i in range(n):
    x, y = map(int, input().split())
    res.append((x, y))

sorted_res = sorted(res, key=lambda x: (x[1], x[0]))

for i in sorted_res:
    print(*i)