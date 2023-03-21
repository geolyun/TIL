n, m = map(int, input().split())

cnt = []

for i in range(1,n+1):
    for j in range(1, m+1):
        cnt.append(i+j)

max_cnt = max(cnt)
b = [0] * max_cnt
for j in cnt:
    b[j-1] += 1

num = 0

for k in b:
    num += 1
    if k == max(b):
        print(num, end=' ')