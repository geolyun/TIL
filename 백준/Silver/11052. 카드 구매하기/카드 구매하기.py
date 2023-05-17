n = int(input())
l = list(map(int, input().split()))

dp = [0, l[0]]
dp.append(max(dp[1]*2, l[1]))

for i in range(3, n+1):
    d = 0
    for j in range(1, i+1):
        d = max(dp[i - j] + l[j-1], d)
    dp.append(d)

print(dp[n])