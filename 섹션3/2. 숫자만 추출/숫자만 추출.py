s = input()

num = []

for i in s:
  if i.isdigit():
    num.append(i)
  else:
    continue

num = ''.join(x for x in num)
num = int(num)

cnt = 0

for i in range(1, num+1):
  if num % i == 0:
    cnt += 1

print(num)
print(cnt)