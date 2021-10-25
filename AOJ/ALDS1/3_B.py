from collections import deque


def main():
    n, q = map(int, input().split())
    dq = deque()
    for _ in range(n):
        name, t = input().split()
        dq.append([name, int(t)])

    time = 0
    while dq:
        name, t = dq.popleft()
        if t <= q:
            time += t
            print(name, str(time))
        else:
            time += q
            t -= q
            dq.append([name, t])


main()
