l1 = []
l2 = []
max = 0

for i in range(15):
  l1.append([" "]*15)

for i in range(5):
  a = list(input())
  l2.append(a)
  if max < len(l2[i]):
    max = len(l2[i])

for i in range(5):
  for j in range(len(l2[i])):
    l1[i][j] = l2[i][j]

for i in range(max):
  for j in range(5):
    if l1[j][i] == " ":
      continue
    else:
      print(l1[j][i], end='')