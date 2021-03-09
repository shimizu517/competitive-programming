n = int(input())
adj_m = [['0'] * n for _ in range(n)]

for _ in range(n):
    l = list(map(int, input().split()))
    for i in range(l[1]):
        adj_m[l[0] - 1][l[i + 2] - 1] = '1'

for i in range(n):
    print(" ".join(adj_m[i]))
