def get_set(a, n):
    _set = set()
    for i in range(2 ** n):
        tmp = 0
        for j in range(i):
            if (1 << j) & i:
                tmp += a[j]
        _set.add(tmp)
    return _set


def main():
    n = int(input())
    a = list(map(int, input().split()))
    _ = int(input())
    m = list(map(int, input().split()))
    _set = get_set(a, n)
    for _m in m:
        print('yes' if _m in _set else 'no')


main()
