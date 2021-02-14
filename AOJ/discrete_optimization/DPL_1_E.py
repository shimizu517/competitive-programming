import sys

sys.setrecursionlimit(500000)
MAX = 10 ** 3 + 1


def bu(s1: str, s2: str):
    dp = [[0] * (len(s2) + 1) for _ in range((len(s1) + 1))]
    for i in range(len(s1) + 1):
        dp[i][0] = i
    for i in range(len(s2) + 1):
        dp[0][i] = i
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            from_top = dp[i - 1][j] + 1
            from_left = dp[i][j - 1] + 1
            from_dia = dp[i - 1][j - 1] + int(s1[i - 1] != s2[j - 1])
            dp[i][j] = min(from_top, from_left, from_dia)

    return dp[len(s1)][len(s2)]


def td(s1: str, s2: str):
    dp = [[MAX] * (len(s2) + 1) for _ in range((len(s1) + 1))]
    for i in range(len(s1) + 1):
        dp[i][0] = i
    for i in range(len(s2) + 1):
        dp[0][i] = i
    result = _rec(len(s1), len(s2), s1, s2, dp)
    return result


def _rec(i: int, j: int, s1: str, s2: str, dp: [[]]):
    if i <= 0 and j <= 0:
        return 0
    if dp[i][j] < MAX:
        return dp[i][j]

    from_top = _rec(i - 1, j, s1, s2, dp) + 1
    from_left = _rec(i, j - 1, s1, s2, dp) + 1
    from_dia = _rec(i - 1, j - 1, s1, s2, dp) + int(s1[i - 1] != s2[j - 1])
    dp[i][j] = min(from_top, from_left, from_dia)
    return dp[i][j]


def main():
    s1, s2 = input(), input()
    # print(bu(s1, s2))
    print(td(s1, s2))


main()
