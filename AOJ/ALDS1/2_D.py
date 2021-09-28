from typing import List

count = 0

# WAだけど理由よく分からん
def insertion_sort(l: List[int], m):
    global count
    n = len(l)
    for i in range(m, n):
        v = l[i]
        j = i - m
        while j >= 0 and l[j] > v:
            l[j + m] = l[j]
            j -= m
            count += 1
        l[j + m] = v


def shell_sort(l):
    n = len(l)
    g = calculate_g(l=l)
    for m in g:
        insertion_sort(l=l, m=m)
    return l, g


def calculate_g(l: List[int]):
    g = 1
    result = [g]
    idx = 0
    while result[idx] <= 100 and result[idx] * 3 + 1 <= len(l):
        result.append(result[idx] * 3 + 1)
        idx += 1
    return list(reversed(result))


def main():
    n = int(input())
    l = []
    for _ in range(n):
        l.append(int(input()))
    l, g = shell_sort(l=l)
    print(len(g))
    print(' '.join(map(str, g)))
    print(count)
    for item in l:
        print(item)


main()
