def sum_digits(num: int, result: int) -> int:
    if num == 0:
        return result
    quotient = num // 10
    remainder = num % 10
    result += remainder
    return sum_digits(quotient, result)


def main():
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if A <= sum_digits(i, 0) <= B:
            ans += i
    print(ans)


main()
