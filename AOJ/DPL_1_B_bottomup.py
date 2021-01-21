n, w = map(int, input().split())
items = [[]]
for i in range(n):
    items.append(list(map(int, input().split())))

c = [[-1] * (w + 1) for _ in range(n + 1)]
for i in range(w + 1):
    c[0][i] = 0

for i in range(n + 1):
    c[i][0] = 0


def knapsak(mw: int, mn: int):
    for w in range(1, mw + 1):
        for i in range(1, mn + 1):
            if w - items[i][1] < 0:
                c[i][w] = c[i - 1][w]
            else:
                c[i][w] = max(c[i - 1][w], c[i - 1][w - items[i][1]] + items[i][0])
    return c[mn][mw]


print(knapsak(w, n))
