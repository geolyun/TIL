n = int(input())
l = list(map(int, input().split()))

dp = [False for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        if dp[i] == False:
            dp[i] = dp[i-j] + l[j-1]
        else:
            dp[i] = min(dp[i], dp[i-j] + l[j-1])

print(dp[n])