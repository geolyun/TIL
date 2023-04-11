ipt = [list(map(int, input().split())) for _ in range(9)]

M = -10000

for i in range(9):
  for j in range(9):
    if ipt[i][j] > M:
      M = ipt[i][j]
      mi = i + 1
      mj = j + 1

print(M)
print(mi, mj)