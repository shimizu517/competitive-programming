n, k = map(int, input().split())


def f(x: int) -> int:
    g1 = int("".join(sorted(str(x), reverse=True)))
    g2 = int("".join(sorted([n for n in str(x) if n != 0])))
    return g1 - g2


ans = n
for i in range(k):
    ans = f(ans)

print(ans)
