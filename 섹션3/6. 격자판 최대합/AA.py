n = int(input())

num = [list(map(int, input().split())) for _ in range(n)]

max = 0

for i in range(n):
  sum = 0
  for j in range(n):
    sum += num[i][j]
    if sum > max:
      max = sum

for i in range(n):
  sum = 0
  for j in range(n):
    sum += num[j][i]
    if sum > max:
      max = sum

sum = 0

for i in range(n):
  for j in range(n):
    if i == j:
      sum += num[i][j]
      if sum > max:
        max = sum

sum = 0

for i in range(n):
  for j in range(n):
    if i + j == 4:
      sum += num[i][j]
      if sum > max:
        max = sum

print(max)
