n = int(input())
result = list(map(int, input().split()))

score = 0

for i in range(len(result)):
  if result[i] == 1:
    score += 1
    for j in range(i+1, len(result)):
      cnt = 0
      if result[j] == 1:
        cnt += 1
        score += cnt
      elif result[j] == 0:
        break

print(score)