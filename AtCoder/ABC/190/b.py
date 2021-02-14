n, s, d = map(int, input().split())


def solve(n, s, d):
    for _ in range(n):
        x, y = map(int, input().split())
        if not (x >= s or y <= d):
            print('Yes')
            return
    print('No')


solve(n, s, d)
