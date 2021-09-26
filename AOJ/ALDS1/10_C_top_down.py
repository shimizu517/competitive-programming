import sys

sys.setrecursionlimit(10 ** 7)


# 遅い。TLEになった
def lcs(x, y, xi, yi, dp):
    if dp[xi][yi] != -1:
        return dp[xi][yi]

    dp[xi][yi] = lcs(x, y, xi - 1, yi - 1, dp) + 1 if x[xi - 1] == y[yi - 1] \
        else max(lcs(x, y, xi, yi - 1, dp), lcs(x, y, xi - 1, yi, dp))
    return dp[xi][yi]


def main():
    n = int(input())
    data_sets = []
    for i in range(n * 2):
        if i % 2 == 0:
            data_sets.append([])
        data_sets[i // 2].append(input())

    for data in data_sets:
        x, y = data
        dp = [[0 if j == 0 or i == 0 else -1 for i in range(len(y) + 1)] for j in range(len(x) + 1)]
        print(lcs(x, y, len(x), len(y), dp))


main()
