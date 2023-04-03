t = int(input())

l = []

for i in range(t):
    w = input()
    l.append(w[0] + w[-1])

for i in l:
    print(i)