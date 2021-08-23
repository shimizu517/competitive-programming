def prime_factorize(n):
    result = []
    base = 2
    while pow(base, 2) <= n:
        if n % base != 0:
            base += 1
            continue
        exp = 0
        while n % base == 0:
            exp += 1
            n //= base
        result.append([base, exp])
        base += 1
    if n > 1:
        result.append([n, 1])
    return result


def main():
    n = int(input())
    result = prime_factorize(n=n)
    if len(result) == 0:
        print(f'{n}: {n}')
        return
    result_str = f'{n}:'
    for base, exp in result:
        for _ in range(exp):
            result_str += f' {base}'
    print(result_str)


main()
