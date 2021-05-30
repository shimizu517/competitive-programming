N, C = map(int, input().split())

abcs = []
for _ in range(N):
    abcs.append(list(map(int, input().split())))


min_d = min([a[0] for a in abcs])
max_d = max([a[1] for a in abcs])

sum = 0
for i in range(min_d, max_d + 1):
    not_prime_sum = 0
    for abc in abcs:
        if abc[0] <= i <= abc[1]:
            not_prime_sum += abc[2]
    sum = sum + C if C <= not_prime_sum else sum + not_prime_sum

print(sum)
