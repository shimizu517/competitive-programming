from typing import List, Tuple


def selection_sort(l: List[int]) -> Tuple[List[int], int]:
    count = 0
    for i in range(len(l)):
        min_j = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_j]:
                min_j = j
        l[i], l[min_j] = l[min_j], l[i]
        if min_j != i:
            count += 1
    return l, count


def main():
    _ = input()
    l = list(map(int, input().split()))
    result, count = selection_sort(l=l)
    print(' '.join(map(str, result)))
    print(count)


main()
