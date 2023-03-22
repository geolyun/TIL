n = int(input())

c = 0

for i in range(2, n+1):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1 
        else:
            continue
    if cnt == 0:
        c += 1
    else:
        continue

print(c)