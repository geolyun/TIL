ans = []

while True:
  dia = []
  sum = 0
  n = int(input())
  if n == -1:
    break
  for i in range(1, n):
    if n % i == 0:
      dia.append(i)
  for i in dia:
    sum += i
  if sum == n:
    ans.append(str(n) + " = " + " + ".join(str(s) for s in dia))
  else:
    ans.append(str(n) + " is NOT perfect.")

for i in ans:
  print(i)