def binary_search(l, key):
    left = -1
    right = len(l)
    while right - left > 1:
        mid = (left + right) // 2
        if l[mid] >= key:
            right = mid
        else:
            left = mid
    return right, l[right] == key


def main():
    n = int(input())
    s = list(map(int, input().split(' ')))
    q = int(input())
    t = list(map(int, input().split(' ')))
    already = set()
    result = 0
    for _t in t:
        if _t in already:
            continue
        min_right, exists = binary_search(l=s, key=_t)
        if exists:
            result += 1
            already.add(_t)
    print(result)


main()
