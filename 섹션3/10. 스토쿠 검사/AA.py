sdk = [list(map(int, input().split())) for _ in range(9)]

def no_duplicates(lst):
    seen = set()
    for element in lst:
        if element in seen:
            return False
        seen.add(element)
    return True

for i in range(9):
  a = []
  b = []
  for j in range(9):
    a.append(sdk[i][j])
    b.append(sdk[j][i])
  if no_duplicates(a) == False or no_duplicates(b) == False:
    print("NO")
    break

else:
  print("YES")
