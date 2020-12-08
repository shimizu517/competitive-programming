N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

Alice_point = sum(A[::2])
Bob_point = sum(A[1::2])

print(Alice_point - Bob_point)
