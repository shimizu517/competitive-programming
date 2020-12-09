def main():
    S = input()
    rwords = list(map(lambda word: word[::-1], ["dream", "dreamer", "erase", "eraser"]))
    rs = S[::-1]
    while True:
        is_ok = False
        for rword in rwords:
            if rs.startswith(rword):
                rs = rs[len(rword) :]
                is_ok = True
        if len(rs) == 0:
            print("YES")
            return
        if not is_ok:
            print("NO")
            return


main()
