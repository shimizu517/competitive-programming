def euclid(x, y):
    if y == 0:
        return x
    return euclid(x=y, y=x % y)


def main():
    x, y = map(int, input().split())
    print(euclid(x=x, y=y))


main()
