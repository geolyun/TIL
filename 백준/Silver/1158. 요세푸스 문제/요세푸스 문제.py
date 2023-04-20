n, k = map(int, input().split())

queue = list(range(1, n+1))
result = []
s = 0

while len(queue) != 1:
  s += k-1
  if s >= len(queue):
    s = s % len(queue)
  result.append(queue.pop(s))

ans = result + queue
print("<" + ', '.join(str(i) for i in ans) + ">")