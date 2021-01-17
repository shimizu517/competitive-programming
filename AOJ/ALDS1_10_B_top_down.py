from pprint import pprint

INF = float("inf")
N = int(input())
p = []
for i in range(N):
    p.append(list(map(int, input().split())))


def memoized_matrix_chain(p):
    n = len(p)
    m = [[0] * n for _ in range(n)]
    # i <= j
    for i in range(n):
        for j in range(i, n):
            m[i][j] = INF
    print(lookup_chain(m, p, 0, n - 1))


def lookup_chain(m, p, i, j):
    if m[i][j] < INF:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = (
                lookup_chain(m, p, i, k)
                + lookup_chain(m, p, k + 1, j)
                + p[i][0] * p[k][1] * p[j][1]
            )
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]


memoized_matrix_chain(p)
