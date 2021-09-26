import sys

sys.setrecursionlimit(10 ** 7)


# 通常の解き方だがTLEしてしまう
def lcs(x, y):
    dp = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[len(x)][len(y)]


def lcs_fast(x, y):
    l = [0] * (len(y) + 1)
    for _x in x:
        l_pre = l[:]
        for j, _y in enumerate(y):
            if _x == _y:
                l[j + 1] = l_pre[j] + 1
            elif l[j + 1] < l[j]:
                l[j + 1] = l[j]
    return l[-1]


def main():
    n = int(input())
    data_sets = []
    for i in range(n * 2):
        if i % 2 == 0:
            data_sets.append([])
        data_sets[i // 2].append(input())

    for data in data_sets:
        x, y = data
        print(lcs_fast(x, y))


main()
