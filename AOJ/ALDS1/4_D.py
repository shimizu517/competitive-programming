# 最大積載量Pの最小値を二分探索で探す
# トラックに対してPの候補P'を割り当てて、それに対して荷物の重さをどんどん引いていく


def solve(n, k, w, r):
    """
    最大積載量Pをmidとして、1台目のトラックに荷物を順番に載せていき全ての荷物を載せきれたら、
    midは十分の最大積載量、つまり多すぎるor必要最低限の値である
        → rightをmidにして、それ以下のPで荷物を載せきれる値を探す
    """
    left = 0
    right = r

    while left < right - 1:
        mid = (left + right) // 2
        is_ok = False
        w_idx = 0
        for i in range(k):
            capacity = mid
            while capacity >= w[w_idx]:
                capacity -= w[w_idx]
                w_idx += 1
                if w_idx >= n:
                    is_ok = True
                    break
            if is_ok:
                break
        if is_ok:
            right = mid
        else:
            left = mid
    return right


def main():
    n, k = map(int, input().split())
    w = []
    right = 0
    for _ in range(n):
        _w = int(input())
        right += _w
        w.append(_w)
    print(solve(n, k, w, right))


main()
