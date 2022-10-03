def climbStairs(n):
    if n<4:
        return n
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
