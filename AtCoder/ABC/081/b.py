def is_divable(A: list, div_num: int) -> bool:
    for a in A:
        if a % div_num != 0:
            return False
    return True


def main():
    N = int(input())
    A = list(map(int, input().split()))

    count = 0
    div_num = 2
    while is_divable(A=A, div_num=div_num):
        count += 1
        div_num *= 2
    print(count)


main()
