def knapsack():
    n, w = map(int, input().split())

    dp = [0] * (w + 1)

    for _ in range(n):
        weight, value = map(int, input().split())
        for j in range(w, 0, -1):
            if j >= weight:
                a, b = dp[j], dp[j - weight] + value
                if a > b:
                    dp[j] = a
                else:
                    dp[j] = b

    print(dp[-1])


knapsack()
