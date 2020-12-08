def main():
    N = int(input())
    A = list(map(int, input().split()))
    sorted_A = sorted(A, reverse=True)
    result = 0
    is_plus: bool = True
    for num in sorted_A:
        result = result + num if is_plus else result - num
        is_plus = not is_plus
    print(result)


main()
