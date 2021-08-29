from collections import deque
from typing import Deque, Dict, List

MAX_N = 100
WHITE = 0
GRAY = 1
BLACK = 2

AdjList = Dict[int, List[int]]


def solve(adj_l: AdjList, n):
    d: Dict[int, int] = {}
    color: Dict[int, int] = {}
    for v_id in adj_l:
        d[v_id] = -1
        color[v_id] = WHITE

    s_id = 1
    q: Deque[int] = deque()
    d[s_id] = 0
    color[s_id] = GRAY
    q.append(s_id)
    while len(q) > 0:
        u_id = q.popleft()
        for v_id in adj_l[u_id]:
            if color[v_id] == WHITE:
                d[v_id] = d[u_id] + 1
                color[v_id] = GRAY
                q.append(v_id)
        color[u_id] = BLACK

    for v_id, _d in d.items():
        print(f'{v_id} {_d}')


def main():
    n = int(input())
    adj_l: AdjList = {}
    for _ in range(n):
        u, k, *v = map(int, input().split())
        adj_l[u] = v
    solve(adj_l=adj_l, n=n)


main()
