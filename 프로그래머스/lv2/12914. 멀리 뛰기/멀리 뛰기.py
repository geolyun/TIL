def solution(n):
    answer = 0
    # dp[1] = 1
    # dp[2] = 2
    # dp[3] = 3
    # dp[4] = 5
    # dp[5] = 8
    
    dp = [0, 1, 2]
    for i in range(3, 2001):
        dp.append(dp[i-1] + dp[i-2])
    
    answer = dp[n] % 1234567
    return answer