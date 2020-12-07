K = 10
count = 0
LunL = list(range(1,10))

while True:
  if K < 10:
    print(LunL[K-1])
    break
  else:
    for i in range(-1,2):
      if (LunL[count]%10 == 0 and i == -1) or (LunL[count]%10 == 9 and i == 1):
        continue
      else:
        LunL.append(LunL[count]*10+i)
        print(LunL)
  count += 1
  if len(LunL) == K:
    print(LunL[K-1])
    break