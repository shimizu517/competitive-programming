from typing import List


def bubble_sort(l: List[int]):
    count = 0
    flag = 1
    while flag:
        flag = 0
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                count += 1
                flag = 1
    return l, count


def main():
    _ = input()
    l = list(map(int, input().split()))
    result, count = bubble_sort(l=l)
    print(' '.join(map(str, result)))
    print(count)


main()
