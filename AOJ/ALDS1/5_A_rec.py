# TLE
def solve(i, a, m, n):
    if m == 0:
        return True
    if i >= n:
        return False
    result = solve(i + 1, a, m, n) or solve(i + 1, a, m - a[i], n)

    return result


def main():
    n = int(input())
    a = list(map(int, input().split()))
    _ = int(input())
    m = list(map(int, input().split()))
    for _m in m:
        print('yes' if solve(0, a, _m, n) else 'no')


main()
