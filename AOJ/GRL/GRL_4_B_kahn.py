from collections import defaultdict, deque
from typing import Dict


def kahn(adj_l: Dict):
    in_degree = defaultdict(int)
    for v, t_list in adj_l.items():
        if v not in in_degree:
            in_degree[v] = 0
        for t in t_list:
            in_degree[t] += 1

    q = deque()
    for v, in_d in in_degree.items():
        if in_d == 0:
            q.append(v)

    result = []
    while len(q) > 0:
        top = q.popleft()
        result.append(top)
        for t in adj_l[top]:
            in_degree[t] -= 1
            if in_degree[t] == 0:
                q.append(t)

    for v, in_d in in_degree.items():
        if in_d != 0:
            raise Exception('graph contains a cycle')

    for v in result:
        print(v)


def main():
    V, E = map(int, input().split())
    adj_l = defaultdict(list)
    for v in range(V):
        adj_l[v] = []
    for _ in range(E):
        s, t = map(int, input().split())
        adj_l[s].append(t)
    kahn(adj_l=adj_l)


main()
