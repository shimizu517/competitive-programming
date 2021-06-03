from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

INF = 10 ** 7


@dataclass
class PrimVertex:
    name: int
    key: int


class MinHeap:
    def __init__(self, initial: Optional[List[PrimVertex]] = None):
        if initial is None:
            initial = []
        self._data: List[PrimVertex] = initial  # [(distance, name)]
        self.pos: Dict[int, int] = {}  # {name: index}

    def get_v_from_name(self, name: int) -> PrimVertex:
        return self._data[self.pos[name]]

    def change_key_using_name(self, name: int, new_key: int):
        idx = self.pos[name]
        self.change_key(i=idx, new_key=new_key)

    def build_min_heap(self):
        for i in range((self.size - 1) // 2, -1, -1):
            self._min_heapify(i=i)

    def insert(self, pv: PrimVertex):
        pv_key = pv.key
        pv.key = INF
        self._data.append(pv)
        self._decrease_key(self.size - 1, pv_key)

    def change_key(self, i: int, new_key: int):
        """
        要素_data[i]のkey属性をnew_keyに変更して順序を入れ替える
        """
        if i < 0 or self.size <= i:
            raise Exception('i is larger than size of heap')
        if self._data[i].key < new_key:
            self._data[i].key = new_key
            self._min_heapify(i=i)
        elif self._data[i].key > new_key:
            self._decrease_key(i=i, key=new_key)
        else:
            print('key is equal to new_key')

    def _decrease_key(self, i: int, key: int):
        """
        _dataのi番目の要素のkeyをkeyに変更して、根に向かって適切な位置まで
        """
        self._data[i].key = key
        self.pos[self._data[i].name] = i
        while i > 0 and self._get_parent(i).key > self._data[i].key:
            self._data[i], self._data[(i - 1) // 2] = self._data[(i - 1) // 2], self._data[i]
            self.pos[self._data[i].name] = i
            self.pos[self._data[(i - 1) // 2].name] = (i - 1) // 2
            i = (i - 1) // 2

    def _min_heapify(self, i: int):
        li = 2 * i + 1
        ri = 2 * i + 2
        min_i = i
        if self.size - 1 >= li and self._data[min_i].key > self._data[li].key:
            min_i = li
        if self.size - 1 >= ri and self._data[min_i].key > self._data[ri].key:
            min_i = ri
        if min_i != i:
            self._data[min_i], self._data[i] = self._data[i], self._data[min_i]
            self.pos[self._data[i].name] = i
            self.pos[self._data[min_i].name] = min_i
            self._min_heapify(i=min_i)

    def extract_min(self) -> PrimVertex:
        _min = self._data[0]
        self._data[0], self._data[self.size - 1] = self._data[self.size - 1], self._data[0]
        del self.pos[_min.name]
        del self._data[self.size - 1]
        if len(self._data) == 1:
            self.pos[self._data[0].name] = 0
        self._min_heapify(i=0)
        return _min

    def has_name(self, name: int) -> bool:
        return name in self.pos

    @property
    def size(self):
        return len(self._data)

    @property
    def is_empty(self):
        return self.size == 0

    def _get_parent(self, i) -> PrimVertex:
        return self._data[(i - 1) // 2]


def prim(adj_l: Dict[int, List[Tuple[PrimVertex, int]]]):
    v_keys = list(adj_l.keys())
    root = v_keys[0]
    pq = MinHeap()

    pq.insert(pv=PrimVertex(name=root, key=v_keys[0]))
    for v in v_keys[1:]:
        pq.insert(PrimVertex(name=v, key=INF))

    ans = 0
    while not pq.is_empty:
        min_v: PrimVertex = pq.extract_min()
        ans += min_v.key
        print(min_v)
        for nei_v, w in adj_l[min_v.name]:
            if pq.has_name(name=nei_v.name) and pq.get_v_from_name(nei_v.name).key > w:
                pq.change_key_using_name(nei_v.name, w)
    return ans


def main():
    V, E = map(int, input().split())
    adj_l: Dict[int, List[tuple]] = defaultdict(list)
    for _ in range(E):
        s, t, w = map(int, input().split())
        adj_l[s].append((PrimVertex(name=t, key=INF), w))
        adj_l[t].append((PrimVertex(name=s, key=INF), w))

    print(prim(adj_l=adj_l))


main()

