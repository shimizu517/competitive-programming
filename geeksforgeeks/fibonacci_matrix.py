def multiply(f: [[]], m: [[]]):
    if len(f[0]) != len(m):
        raise Exception('Unable to calculate.')
    result = [[0] * len(m[0]) for _ in range(len(f))]
    for i in range(len(f)):
        for j in range(len(m[0])):
            for k in range(len(m)):
                result[i][j] += f[i][k] * m[k][j]
    return result


def power(f, n):
    m = [[1, 1],
         [1, 0]]
    for i in range(2, n + 1):
        m = multiply(f, m)
    return m


def fib(n):
    f = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    result = power(f, n - 1)
    return result[0][0]


print(fib(9))
