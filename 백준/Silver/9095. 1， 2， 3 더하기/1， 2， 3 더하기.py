s = [0, 1, 2, 4]
for i in range(3, 11):
    s.append(s[i]+s[i-1]+s[i-2])

T = int(input())
for i in range(T):
    n = int(input())
    print(s[n])

# dp[0] = 0
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4
# dp[4] = 7
# dp[5] = 13
# dp[6] = 24
# dp[7] = 44