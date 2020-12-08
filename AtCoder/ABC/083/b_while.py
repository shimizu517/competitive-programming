def sum_of_each_digits(num: int):
    result = 0
    while True:
        if num == 0:
            return result
        result += num % 10
        num = num // 10


def main():
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if A <= sum_of_each_digits(i) <= B:
            ans += i
    print(ans)


main()
