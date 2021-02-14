import sys

sys.setrecursionlimit(500000)


def bu(n, w, vw):
    max_v = sum(v for v, w in vw)
    # dp[i]=価値の総和がiになるときの最小限の重さ
    # dpの中で要素の大きさがwを超えない最大のiが答え
    dp = [w + 1] * (max_v + 1)
    dp[0] = 0
    for v, j in vw:
        for i in range(max_v, -1, -1):
            dp[i] = min(dp[i - v] + j, dp[i])
    return max(i for i in range(max_v + 1) if dp[i] <= w)


def main():
    n, w = map(int, input().split())
    vw = [list(map(int, input().split())) for _ in range(n)]
    print(bu(n, w, vw))


main()
