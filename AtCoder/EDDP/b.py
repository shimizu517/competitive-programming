def main():
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))

    inf = float("inf")
    dp = [inf] * n
    dp[0] = 0
    for i in range(1, n):
        dp[i] = min(dp[j] + abs(lst[i] - lst[j]) for j in range(max(i - k, 0), i))
    print(dp[-1])


main()
