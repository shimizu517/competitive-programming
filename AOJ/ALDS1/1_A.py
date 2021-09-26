from typing import List


def insert_sort(l: List[int]):
    for i in range(1, len(l)):
        v = l[i]
        j = i - 1
        while l[j] > v and j >= 0:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = v
        print(' '.join(map(str, l)))


def main():
    _ = int(input())
    l = list(map(int, input().split()))
    print(' '.join(map(str, l)))
    insert_sort(l=l)


main()
