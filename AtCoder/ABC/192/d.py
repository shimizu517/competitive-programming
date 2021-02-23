def from_base_to_decimal(base, num):
    res = 0
    cnt = 0
    while num >= 1:
        res += num % 10 * pow(base, cnt)
        num //= 10
        cnt += 1
    return res


def main():
    x = int(input())
    m = int(input())
    maxi = max([int(_x) for _x in str(x)])
    if x <= 9:
        if x <= m:
            print(1)
            return
        else:
            print(0)
            return

    ok = maxi
    ng = 1000000000000000001
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if from_base_to_decimal(mid, x) <= m:
            ok = mid
        else:
            ng = mid
    print(ok - maxi)


main()
