INF = 10 ** 20


def floyd_warchall(adj_m, V):
    p = [[INF] * V for _ in range(V)]
    tmp = [[INF] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i == j:
                adj_m[i][j] = 0
            tmp[i][j] = adj_m[i][j]

    for k in range(V):
        tmp_after = [[INF] * V for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if tmp[i][k] == INF or tmp[k][j] == INF:
                    tmp_after[i][j] = tmp[i][j]
                    continue
                if tmp[i][k] + tmp[k][j] < tmp[i][j]:
                    tmp_after[i][j] = tmp[i][k] + tmp[k][j]
                else:
                    tmp_after[i][j] = tmp[i][j]

        for i in range(V):
            for j in range(V):
                tmp[i][j] = tmp_after[i][j]

    rows = []
    for i in range(V):
        rows.append([str(item) if item != INF else 'INF' for item in tmp[i]])
        if tmp[i][i] < 0:
            print('NEGATIVE CYCLE')
            return
    for i in range(V):
        print(' '.join(rows[i]))


def main():
    V, E = map(int, input().split())
    adj_m = [[INF] * V for _ in range(V)]
    for _ in range(E):
        s, t, d = map(int, input().split())
        adj_m[s][t] = d
    floyd_warchall(adj_m=adj_m, V=V)


main()
