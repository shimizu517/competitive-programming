from pprint import pprint

n, w = map(int, input().split())
items = [[]]
for i in range(n):
    items.append(list(map(int, input().split())))

c = [[-1] * (w + 1) for _ in range(n + 1)]
for i in range(w + 1):
    c[0][i] = 0

for i in range(n + 1):
    c[i][0] = 0


def knapsak(w: int, k: int):
    if k <= 0 or i <= 0:
        return 0
    if c[k][w] >= 0:
        return c[k][w]

    if w - items[k][1] < 0:
        c[k][w] = knapsak(w, k - 1)
        return c[k][w]
    else:
        c[k][w] = max(knapsak(w, k - 1), knapsak(w - items[k][1], k - 1) + items[k][0])
        return c[k][w]


print(knapsak(w, n))

pprint(c)
