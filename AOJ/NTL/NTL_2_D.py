a,b = map(int,input().split())
c = abs(a) // abs(b)
print(-c if a * b < 0 else c)