n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in range(10):
    s, e = map(int, input().split())
    n = n[:s-1] + list(reversed(n[s-1:e])) + n[e:]

for i in range(len(n)):
    print(n[i], end=' ')