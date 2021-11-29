from collections import defaultdict
from typing import List, Dict


class El:
    def __init__(self, key: int, data: str):
        self.key: int = key
        self.data = data

    def __str__(self):
        return f'{self.data} {self.key}'


def partition(a: List[El], l, r):
    """
    pre: l < r
    """
    pivot = a[r].key
    idx = l - 1
    for i in range(l, r + 1):
        if a[i].key <= pivot:
            idx += 1
            a[i], a[idx] = a[idx], a[i]
    return idx


def quick_sort(a: List[El], l, r):
    if l < r:
        mid = partition(a, l, r)
        quick_sort(a, l, mid - 1)
        quick_sort(a, mid + 1, r)


def order_el(a: List[El]):
    d = defaultdict(list)
    for _a in a:
        d[_a.key].append(_a.data)
    return d


def check(a: List[El], d: Dict[int, List[str]]):
    idx_d = defaultdict(int)
    for _a in a:
        idx = idx_d[_a.key]
        if d[_a.key][idx] != _a.data:
            return False
        idx_d[_a.key] += 1
    return True


def main():
    n = int(input())
    a: List[El] = []
    for _ in range(n):
        data, key = input().split(' ')
        a.append(El(key=int(key), data=data))
    d = order_el(a)
    quick_sort(a, 0, len(a) - 1)
    is_stable = check(a, d)
    print('Stable' if is_stable else 'Not stable')
    for _a in a:
        print(f'{_a.data} {_a.key}')


main()
