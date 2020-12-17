def main():
    N, W = map(int, input().split())
    w, v = [0] * (N + 1), [0] * (N + 1)
    for i in range(1, N + 1):
        w[i], v[i] = map(int, input().split())
    V = sum(v)
    dp = [10 ** 9] * (V + 1)
    dp[0] = 0

    vsum = 0
    for i in range(1, N + 1):
        for j in range(vsum + v[i], 0, -1):
            if j >= v[i]:
                a, b = dp[j], dp[j - v[i]] + w[i]
                if a < b:
                    dp[j] = a
                else:
                    dp[j] = b
            else:
                dp[j] = dp[j]
        vsum += v[i]

    print(max(j for j in range(V + 1) if dp[j] <= W))


main()
