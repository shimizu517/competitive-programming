def main():
    N = int(input())
    H = list(map(int, input().split()))
    dp = [10 ** 4] * N
    dp[0] = 0
    for i in range(N - 1):
        dp[i + 1] = min(abs(H[i + 1] - H[i]) + dp[i], dp[i + 1])
        if i <= N - 3:
            dp[i + 2] = min(abs(H[i + 2] - H[i]) + dp[i], dp[i + 2])
    print(dp[N - 1])


main()
