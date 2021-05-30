W = int(input())
N, K = map(int, input().split())
Items = [list(map(int, input().split())) for _ in range(N)]
MAX_V = 50 * 100
INF = 10 ** 9

# dp[i][k][v] := i番目まで見てk個選んだ時に価値の総和がvになるために必要な最小幅合計
dp = [[[INF] * (MAX_V + 1) for j in range(K + 1)] for i in range(N + 1)]
dp[0][0][0] = 0
for i, (a, b) in enumerate(Items):
    for k in range(K + 1):
        for v in range(MAX_V + 1):
            dp[i + 1][k][v] = min(dp[i + 1][k][v], dp[i][k][v])
            if v + b <= MAX_V and k + 1 <= K:
                dp[i + 1][k + 1][v + b] = min(dp[i + 1][k + 1][v + b], dp[i][k][v] + a)

ans = 0
for k in range(K + 1):
    for v in range(MAX_V + 1):
        if dp[-1][k][v] <= W:
            ans = max(ans, v)
print(ans)
W = int(input())
N, K = map(int, input().split())
Items = [list(map(int, input().split())) for _ in range(N)]
MAX_V = 50 * 100
INF = 10 ** 9

# dp[i][k][v] := i番目まで見てk個選んだ時に価値の総和がvになるために必要な最小幅合計
dp = [[[INF] * (MAX_V + 1) for j in range(K + 1)] for i in range(N + 1)]
dp[0][0][0] = 0
for i, (a, b) in enumerate(Items):
    for k in range(K + 1):
        for v in range(MAX_V + 1):
            dp[i + 1][k][v] = min(dp[i + 1][k][v], dp[i][k][v])
            if v + b <= MAX_V and k + 1 <= K:
                dp[i + 1][k + 1][v + b] = min(dp[i + 1][k + 1][v + b], dp[i][k][v] + a)

ans = 0
for k in range(K + 1):
    for v in range(MAX_V + 1):
        if dp[-1][k][v] <= W:
            ans = max(ans, v)
print(ans)
