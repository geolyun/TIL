n = int(input())

result = []

for i in range(n):
  word = input()
  word = word.lower()
  if word == word[::-1]:
    result.append("YES")
  else:
    result.append("NO")

for i in range(len(result)):
  print("#%s %s" % (i+1, result[i]))