n = int(input())

num = [list(map(int, input().split())) for _ in range(n)]

num.insert(0, [0]*n)
num.append([0]*n)

for x in num:
  x.insert(0, 0)
  x.append(0)

cnt = 0

for i in range(1, n+1):
  for j in range(1, n+1):
    if num[i][j] > num[i+1][j] and num[i][j] > num[i-1][j] and num[i][j] > num[i][j+1] and num[i][j] > num[i][j-1]:
      cnt += 1

print(cnt)
