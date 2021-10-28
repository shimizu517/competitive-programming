def binary_search(l, key):
    left = 0
    right = len(l)
    while left < right:
        mid = (right + left) // 2
        if l[mid] == key:
            return True
        if l[mid] < key:
            left = mid + 1
        if key < l[mid]:
            right = mid
    return False


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
        if binary_search(l=s, key=_t):
            result += 1
            already.add(_t)
    print(result)


main()
