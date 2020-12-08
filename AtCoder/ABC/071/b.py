from string import ascii_lowercase as al


def main():
    S = input()
    ascii_lower_dict = {alp: False for alp in al}
    for alpha in S:
        ascii_lower_dict[alpha] = True
    for alpha in al:
        if not ascii_lower_dict[alpha]:
            print(alpha)
            return
    print("None")


main()
