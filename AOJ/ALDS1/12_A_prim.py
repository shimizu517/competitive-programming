import heapq
from typing import List

INF = 10000


class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix: List[List[int]] = adj_matrix

    def mst_prim(self) -> int:
        result = 0
        vertex_count = len(self.adj_matrix)
        used = [False for _ in range(vertex_count)]
        Q = []
        # (weight_to_mst, idx)
        heapq.heappush(Q, (0, 0))
        while len(Q) > 0:
            weight, u_id = heapq.heappop(Q)
            if used[u_id]:
                continue
            used[u_id] = True
            result += weight
            for idx, w in enumerate(self.adj_matrix[u_id]):
                if w == -1 or used[idx]:
                    continue
                heapq.heappush(Q, (w, idx))
        return result


def main():
    n = int(input())
    adj_matrix = []
    for _ in range(n):
        adj_matrix.append(list(map(int, input().split())))
    g = Graph(adj_matrix)
    print(g.mst_prim())


main()
