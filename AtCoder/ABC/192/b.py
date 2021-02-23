s = input()


def check(s: str):
    for i, c in enumerate(s):
        if i % 2 == 0 and c.isupper():
            print('No')
            return
        elif i % 2 == 1 and c.islower():
            print('No')
            return
    print('Yes')


check(s)
