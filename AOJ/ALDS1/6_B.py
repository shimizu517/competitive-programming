def partition_str(a, p, r):
    v = a[r]
    idx = p - 1
    for i in range(p, r + 1):
        if a[i] <= v:
            idx += 1
            if i == r:
                a[idx], a[i] = f'[{str(a[i])}]', a[idx]
            else:
                a[idx], a[i] = a[i], a[idx]
    return list(map(str, a))


def main():
    _ = input()
    a = list(map(int, input().split(' ')))
    r = len(a) - 1
    result = partition_str(a, 0, r)
    print(' '.join(result))


main()
