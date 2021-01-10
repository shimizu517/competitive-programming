inp = 10

l = []
mult = 1

for i in range(inp,1, -1):
  if len(l) == 0:
    l.append(i)
    mult *= i
    continue
  if mult % i != 0:
    l.append(i)
    mult *= i

print(mult + 1)

# ans = 1
# for item in l:
#   ans *= item
# print()