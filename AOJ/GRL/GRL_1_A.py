from heapq import heappush, heappop

INF = 10 ** 9


def relax(d, v, u, w):
    if d[u] >= d[v] + w:
        d[u] = d[v] + w
        return d[u]
    return False


def dijkstra(adj_l, s):
    d = [INF for _ in range(len(adj_l))]
    d[s] = 0
    q = []
    heappush(q, (0, s))
    while q:
        _d, t = heappop(q)
        for u, w in adj_l[t]:
            if d[u] > _d + w:
                d[u] = _d + w
                heappush(q, (d[u], u))

    for w in d:
        print('INF') if w == INF else print(w)


def main():
    V, E, r = map(int, input().split())
    adj_l = [[] for _ in range(V)]
    for _ in range(E):
        s, t, d = map(int, input().split())
        adj_l[s].append([t, d])

    dijkstra(adj_l=adj_l, s=r)


main()
