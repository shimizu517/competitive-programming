N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0
for i in range(N):
    sum += A[i] * B[i]

print("Yes") if sum == 0 else print("No")
