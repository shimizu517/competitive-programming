def naive_string_matcher(t: str, p: str):
    n, m = map(len, (t, p))
    for s in range(n - m + 1):
        if t[s:s + m] == p:
            print(s)


def main():
    T = input()
    P = input()
    naive_string_matcher(T, P)


main()
