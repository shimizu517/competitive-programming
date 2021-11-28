N = 10000


def counting_sort(a):
    result = [0 for _ in range(len(a))]
    c = [0 for _ in range(N + 1)]
    for _a in a:
        c[_a] += 1
    for i in range(1, N+1):
        c[i] += c[i - 1]
    for i in range(len(a) - 1, -1, -1):
        _a = a[i]
        result[c[_a] - 1] = _a
        c[_a] -= 1
    return result


def main():
    _ = int(input())
    a = list(map(int, input().split(' ')))
    result = counting_sort(a=a)
    print(' '.join(map(str, result)))


main()
