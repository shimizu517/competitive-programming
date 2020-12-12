# 入力の順番に旅行しないといけないのを見逃していたためWA

from typing import NamedTuple, List


class Txy(NamedTuple):
    t: int
    x: int
    y: int


def main():
    N = int(input())
    l: List[Txy] = []
    for _ in range(N):
        l.append(Txy(*tuple(map(int, input().split()))))

    for txy in l:
        if txy.x + txy.y > txy.t:
            print("No")
            return
        if txy.t % 2 == (txy.x + txy.y) % 2:
            continue
        print("No")
        return

    print("yes")


main()
