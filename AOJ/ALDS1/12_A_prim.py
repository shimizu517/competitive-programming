import heapq


class Prim:
    INF = 2001

    def __init__(self):
        pass

    def execute(self, adj_matrix):
        q = []
        d = [self.INF for _ in range(len(adj_matrix))]
        used = [False for _ in range(len(adj_matrix))]
        d[0] = 0
        # (d[key], key)
        heapq.heappush(q, (0, 0))
        result = 0

        while len(q) > 0:
            _w, u = heapq.heappop(q)
            if used[u]:
                continue
            used[u] = True
            result += _w
            for idx, weight in enumerate(adj_matrix[u]):
                if weight == -1:
                    continue
                if weight < d[idx]:
                    d[idx] = weight
                    heapq.heappush(q, (weight, idx))
        return result


def main():
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))
    p = Prim()
    print(p.execute(adj_matrix=adj_matrix))


main()
