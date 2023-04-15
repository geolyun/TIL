n = int(input())
n = str(n)

l = []

for i in n:
    l.append(int(i))

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]

for i in l:
    print(i, end='')