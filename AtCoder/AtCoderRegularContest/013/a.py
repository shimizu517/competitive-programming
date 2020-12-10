def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    i = 0
    while i < N:
        while i + 1 < N and A[i] == A[i + 1]:  # これはA[0]から連続で同じ値が続くときだけ動く
            i += 1
        if i + 1 < N and A[i] < A[i + 1]:
            while i + 1 < N and A[i] <= A[i + 1]:
                i += 1
        elif i + 1 < N and A[i] > A[i + 1]:
            while i + 1 < N and A[i] >= A[i + 1]:
                i += 1
        count += 1
        i += 1
    print(count)


main()

# 参考：https://drken1215.hatenablog.com/entry/2019/03/28/014100
