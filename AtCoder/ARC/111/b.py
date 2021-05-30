from dataclasses import dataclass
from typing import Any, Dict, List, NamedTuple, Optional, TypeVar, Union
from pprint import pprint
from enum import Enum

MAX_V = 400001


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


@dataclass
class Vertex:
    val: int
    color: Color
    pre: List["Vertex"]  # precedessor
    d: Optional[int] = None  # discovery time
    f: Optional[int] = None  # finishing time


T_ADJ = List[List[Vertex]]
adj: T_ADJ = [[] for _ in range(MAX_V)]
vertices: Dict[int, Vertex] = {}


def dfs(adj: T_ADJ):
    is_cycle: bool = True
    graph_sets: List[List[Union[bool, int]]] = []
    for u in vertices.values():
        if u.color == Color.WHITE:
            is_cycle, v_len = dfs_visit(adj, u, is_cycle, 1)
            graph_sets.append([is_cycle, v_len])
    return graph_sets


def dfs_visit(adj: T_ADJ, u: Vertex, is_cycle: bool, v_len: int):
    u.color = Color.GRAY
    for v in adj[u.val]:
        if v.color == Color.WHITE:
            v_len += 1
            is_cycle, v_len = dfs_visit(adj, v, is_cycle, v_len)
        elif v.color == Color.GRAY:
            u.pre.append(v)
            is_cycle = len(u.pre) > 1
    u.color = Color.BLACK
    return is_cycle, v_len


def main():
    N = int(input())

    for _ in range(N):
        a, b = list(map(int, input().split()))
        if a not in vertices:
            vertices[a] = Vertex(val=a, pre=[], color=Color.WHITE)
        if b not in vertices:
            vertices[b] = Vertex(val=b, pre=[], color=Color.WHITE)
        adj[a].append(vertices[b])
        adj[b].append(vertices[a])
    graph_sets = dfs(adj)
    sum = 0
    for graph_set in graph_sets:
        print(graph_sets)
        sum += graph_set[1] if graph_set[0] else graph_set[1] - 1
    print(sum)


main()
