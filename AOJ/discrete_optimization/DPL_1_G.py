N, W = map(int, input().split())
dp = [0] * (W + 1)
max_w = 0
for i in range(N):
    v, w, m = map(int, input().split())
    n = 1
    while m > 0:
        m -= n
        _v, _w = v * n, w * n
        # ↓はmax_w = Wでもおっけー。でも↓のほうが高速。
        # max_w = min(max_w + _w, W)
        max_w = W
        for k in range(max_w, _w - 1, -1):
            if dp[k] < dp[k - _w] + _v:
                dp[k] = dp[k - _w] + _v
        # ↓で高速化しているっぽい。↓が無いとTLEになる
        n = min(m, n << 1)

print(max(dp))
