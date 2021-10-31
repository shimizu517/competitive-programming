def cost(n, p, q, i, j):
    print('cost')
    if i - 1 == j:
        return q[j]
    _sum = sum(p[i:j]) + sum(q[i - 1:j])
    _min = 10 ** 7
    for r in range(i, j):
        val = cost(n, p, q, i, r - 1) + cost(n, p, q, r + 1, j)
        _min = min(_min, val)
    if i == j:
        _min = q[i-1] + q[i] + p[i]
    return _min + _sum + 1


def main():
    print('start')
    n = int(input())
    p = [-1.0] + list(map(float, input().split()))
    q = list(map(float, input().split()))

    print(cost(n, p, q, 1, n + 1))


main()
