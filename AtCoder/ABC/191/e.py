n, m = map(int, input().split())

adj_l = [[0, 0]] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    if adj_l[a] == [0, 0]:
        adj_l[a] = [[b, c]]
    else:
        adj_l[a].append([b, c])

print(adj_l)
