def main():
    n = int(input())
    _set = set()
    for _ in range(n):
        command, key = tuple(input().split(' '))
        if command == 'insert':
            _set.add(key)
        elif command == 'find':
            print('yes' if key in _set else 'no')


main()
