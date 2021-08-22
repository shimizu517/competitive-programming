def power(m, n, mod) -> int:
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(m=m, n=n / 2, mod=mod) ** 2 % mod
    else:
        return m * power(m=m, n=n // 2, mod=mod) ** 2 % mod


def main():
    m, n = map(int, input().split())
    mod = 1_000_000_007
    print(power(m=m, n=n, mod=mod))


main()
