a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

n = n0

if a1 * n + a0 <= c * n and c>=a1:
    print(1)
else:
    print(0)