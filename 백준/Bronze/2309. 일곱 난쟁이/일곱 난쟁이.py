li = []

for i in range(9):
    h = int(input())
    li.append(h)

li.sort()
s = sum(li)

for i in range(9):
    for j in range(i+1, 9):
        s2 = s - li[i] - li[j]
        if s2 == 100:
            rset = {li[i], li[j]}

li2 = [i for i in li if i not in rset]
print(*li2, sep='\n')