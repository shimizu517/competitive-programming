from collections import deque
from typing import List, Deque

INF = 10 ** 9


class EdmondsKarp:
    def __init__(self, residual_graph, V):
        self.residual_graph: List[List[int]] = residual_graph
        self.V = V

    def bfs(self, source: int, sink: int, parent: List[int]):
        queue: Deque[int] = deque()
        visited = [False] * self.V
        visited[source] = True
        queue.append(source)
        while len(queue) > 0:
            s = queue.popleft()
            for t, c in enumerate(self.residual_graph[s]):
                if c != 0 and not visited[t]:
                    queue.append(t)
                    visited[t] = True
                    parent[t] = s
                    if t == sink:
                        return True
        return False

    def execute(self, source, sink):
        max_flow = 0
        parent: List[int] = [-1] * self.V

        # whileでmax_flowを求める
        # parentに
        while self.bfs(source=source, sink=sink, parent=parent):
            s = sink
            path_flow = INF
            while s != source:
                # sの親からsへの残余容量のうち小さい方をmax_flowとする
                path_flow = min(path_flow, self.residual_graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow

            s = sink
            while s != source:
                s_parent = parent[s]
                self.residual_graph[s_parent][s] -= path_flow
                self.residual_graph[s][s_parent] += path_flow
                s = s_parent

        return max_flow


def main():
    V, E = map(int, input().split())
    # 隣接行列の残余グラフ
    residual_graph = [[0] * V for _ in range(V)]
    for _ in range(E):
        u, v, c = map(int, input().split())
        residual_graph[u][v] = c

    edmonds_karp = EdmondsKarp(residual_graph=residual_graph, V=V)
    print(edmonds_karp.execute(source=0, sink=V - 1))


main()
