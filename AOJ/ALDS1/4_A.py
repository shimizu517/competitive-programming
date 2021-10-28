from copy import copy


def linear_search(l, n, key):
    _l = copy(l)
    _l.append(key)
    i = 0
    while _l[i] != key:
        i += 1
    return i != n


def main():
    n = int(input())
    s = list(map(int, input().split(' ')))
    q = int(input())
    t = list(map(int, input().split(' ')))
    result = 0
    already = set()
    for _t in t:
        if _t in already:
            continue
        if linear_search(l=s, n=n, key=_t):
            result += 1
            already.add(_t)
    print(result)


main()
