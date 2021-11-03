INF = 10 ** 9 + 1

count = 0


def merge(a, left, mid, right):
    global count
    L = a[left:mid] + [INF]
    R = a[mid:right] + [INF]
    li = ri = 0
    for i in range(left, right):
        count += 1
        if L[li] <= R[ri]:
            a[i] = L[li]
            li += 1
        else:
            a[i] = R[ri]
            ri += 1


def merge_sort(a, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid, right)
        return merge(a, left, mid, right)


def main():
    n = int(input())
    s = list(map(int, input().split(' ')))

    global count
    merge_sort(s, 0, len(s))
    print(' '.join(map(str, s)))
    print(count)


main()
