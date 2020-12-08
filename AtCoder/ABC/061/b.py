def main():
    N, M = list(map(int, input().split()))
    city_pairs = []
    for _ in range(M):
        n_m = list(map(int, input().split()))
        city_pairs.append(n_m)
    ans = [0] * N
    for city_pair in city_pairs:
        ans[city_pair[0] - 1] += 1
        ans[city_pair[1] - 1] += 1

    for a in ans:
        print(a)

main()
