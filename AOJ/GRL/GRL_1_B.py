INF = 10 ** 7
NEGATIVE = 'NEGATIVE CYCLE'
INF_STR = 'INF'


def bellman_ford(adj_l, V, E, s):
    d = [INF] * V
    d[s] = 0
    has_negative_cycle = False
    for _ in range(V - 1):
        for i, edges in enumerate(adj_l):
            for e in edges:
                relax(i, e[0], e[1], d)

    for v, edges in enumerate(adj_l):
        for edge in edges:
            if d[v] in [INF, NEGATIVE] or d[edge[0]] == NEGATIVE:
                continue
            if d[edge[0]] > d[v] + edge[1]:
                d[edge[0]] = NEGATIVE
                has_negative_cycle = True

    if has_negative_cycle:
        print(NEGATIVE)
    else:
        print_bellman_ford(d=d)


def relax(u, v, w, d):
    if d[v] > d[u] + w and d[u] != INF:
        d[v] = d[u] + w


def print_bellman_ford(d):
    for el in d:
        print(el) if el != INF else print(INF_STR)


def main():
    V, E, r = map(int, input().split())
    adj_l = [[] for _ in range(V)]
    # d[i]は始点sから頂点viへの最短路の上界
    for _ in range(E):
        s, t, d = map(int, input().split())
        adj_l[s].append([t, d])

    bellman_ford(adj_l=adj_l, V=V, E=E, s=r)


main()
