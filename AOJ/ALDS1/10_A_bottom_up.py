def fibonacci(n, dp):
    if n <= 1:
        return 1
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n]


def main():
    n = int(input())
    dp = [None] * (n + 1)
    print(fibonacci(n=n, dp=dp))


main()
