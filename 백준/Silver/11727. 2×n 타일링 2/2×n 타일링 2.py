s = [0, 1, 3, 5, 11, 21]
for i in range(6, 1001):
    s.append(s[i-2]*2 + s[i-1])
n = int(input())
print(s[n]%10007)

# dp[0] - 0
# dp[1] - 1
# dp[2] - 3
# dp[3] - 5
# dp[4] - 11
# dp[5] - 21
# dp[3]부터는 dp[1]*2 + dp[2] = dp[3]같은 규칙 