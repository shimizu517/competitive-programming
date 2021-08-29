def fibonacci(n, dp):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif dp[n] is not None:
        return dp[n]
    dp[n] = fibonacci(n=n - 1, dp=dp) + fibonacci(n=n - 2, dp=dp)
    return dp[n]


def main():
    n = int(input())
    dp = [None] * (n + 1)
    print(fibonacci(n=n, dp=dp))


main()
