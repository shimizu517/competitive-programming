from typing import NamedTuple, List


class Txy(NamedTuple):
    t: int
    x: int
    y: int


def can_stop_on_point(txy_cur: Txy, txy_next: Txy) -> bool:
    dist = abs(txy_next.x - txy_cur.x) + abs(txy_next.y - txy_cur.y)
    t_diff = txy_next.t - txy_cur.t  # txy_next.t > txy_curである
    if dist > t_diff:
        return False
    if dist % 2 == t_diff % 2:
        return True
    return False


def main():
    N = int(input())
    l: List[Txy] = []
    txy_cur: Txy = Txy(0, 0, 0)
    for _ in range(N):
        txy_next = Txy(*tuple(map(int, input().split())))
        if not can_stop_on_point(txy_cur, txy_next):
            print("No")
            return
        txy_cur = txy_next
    print("Yes")


main()
