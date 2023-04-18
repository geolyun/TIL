n = int(input())

res = []

for i in range(n):
    word = input()
    res.append(word)

res = set(res)
res = list(res)

sorted_res = sorted(res, key = lambda x : (len(x), x))

for i in sorted_res:
    print(i)