def get_num_of_divisor(k):
    result = 0
    sq = int(k ** 0.5)
    for i in range(1, sq + 1):
        if k % i == 0:
            result += 2
    return result - (sq * sq == k)


def main():
    n = int(input())
    while n % 2 == 0:
        n = int(n / 2)

    print(2 * get_num_of_divisor(n))


main()
