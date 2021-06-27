from collections import defaultdict, deque
from typing import Optional

WHITE = 0
GRAY = 1
BLACK = 2

count = 0


# あるノードに隣接するすべてのノードを1つずつ見つける
def get_next(v, adj_l, idx) -> Optional[int]:
    if len(adj_l[v]) <= idx:
        return None
    return adj_l[v][idx]


def dfs_visit(adj_l, d, f, color, v):
    global count
    stack = deque()
    idx_dict = {v: 0 for v in adj_l}
    stack.append(v)
    color[v] = GRAY
    d[v] = count

    while stack:
        t = stack[-1]
        u = get_next(v=t, adj_l=adj_l, idx=idx_dict[t])
        idx_dict[t] += 1
        if u is not None:
            if color[u] == WHITE:
                count += 1
                d[u] = count
                color[u] = GRAY
                stack.append(u)
        else:
            color[t] = BLACK
            count += 1
            f[t] = count
            stack.pop()


def dfs(adj_l):
    d = {v: 0 for v in adj_l}
    f = {v: 0 for v in adj_l}
    color = {v: WHITE for v in adj_l}
    for v in adj_l:
        if color[v] == WHITE:
            global count
            count += 1
            dfs_visit(adj_l=adj_l, d=d, f=f, color=color, v=v)

    for v in adj_l:
        print(v, d[v], f[v])


def main():
    n = int(input())
    adj_l = defaultdict(list)
    for _ in range(n):
        u, k, *l = map(int, input().split())
        adj_l[u] = l

    dfs(adj_l=adj_l)


main()
