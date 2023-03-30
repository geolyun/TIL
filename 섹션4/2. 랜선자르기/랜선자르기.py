k, n = map(int, input().split())

J = []
result = []

for i in range(k):
    l = int(input())
    J.append(l)

for i in range(1, 1000000):
    cnt = 0
    for j in range(k):
        cnt += J[j] // i
        if cnt == n:
            result.append(i)

print(result[-1])