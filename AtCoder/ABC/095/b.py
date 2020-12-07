def main():
    N, X = tuple(map(int, input().split()))
    M = []
    for i in range(N):
        M.append(int(input()))
    ans = 0
    for m in M:
        X -= m
        ans += 1
    minm = min(M)
    ans += X // minm
    print(ans)


main()
