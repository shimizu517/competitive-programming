import math

A = [1, 6, 4, 2, 7, 19, 9, 5, 3]
MAX = 10 ** 5


def merge_sort(a, l, mid, r):
    L = []
    R = []
    for i in range(l, mid + 1):
        L.append(a[i])
    L.append(MAX)
    for i in range(mid + 1, r + 1):
        R.append(a[i])
    R.append(MAX)

    j, k = 0, 0
    for i in range(l, r + 1):
        if L[j] > R[k]:
            A[i] = R[k]
            k += 1
        else:
            A[i] = L[j]
            j += 1


def merge(a, l, r):
    if r > l:
        mid = math.floor((r + l) / 2)
        merge(a, l, mid)
        merge(a, mid + 1, r)
        merge_sort(a, l, mid, r)


# l <= mid < r
merge(A, 0, len(A) - 1)
print(A)
