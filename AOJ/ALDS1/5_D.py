count = 0
INF = 10 ** 10

inv_cnt = 0


def merge_sort(a, left, right):
    if left < right - 1:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid, right)
        merge(a, left, mid, right)


def merge(a, left, mid, right):
    global count, inv_cnt
    l = []
    for i in range(left, mid):
        l.append(a[i])
    l.append(INF)

    r = []
    for i in range(mid, right):
        r.append(a[i])
    r.append(INF)

    il = ir = 0
    cnt = len(l) - 1
    for i in range(left, right):
        if l[il] <= r[ir]:
            a[i] = l[il]
            il += 1
            cnt -= 1
        else:
            a[i] = r[ir]
            ir += 1
            inv_cnt += cnt


def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    merge_sort(a=a, left=0, right=len(a))
    print(inv_cnt)


main()
