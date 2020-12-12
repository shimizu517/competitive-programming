def main():
    N = int(input())
    h = list(map(int, input().split()))
    dp = [10 ** 4] * N
    dp[0] = 0
    for i in range(1, N):
        if i < 2:
            dp[i] = dp[i - 1] + abs(h[i] - h[i - 1])
        else:
            dp[i] = min(
                dp[i - 1] + abs(h[i - 1] - h[i]), dp[i - 2] + abs(h[i - 2] - h[i])
            )
    print(dp[:N])
    print(dp[N - 1])


main()
