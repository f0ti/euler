#!/usr/bin/env python3

m = []
i = 10

while i < 200000:
  i += 1
  print(i)
  not_prime = 0
  for j in range(2, i):
    if i%j == 0:
      not_prime = 1
      break
  if not_prime == 0:
    m.append(i)

b = False
f = []

while len(f) < 11:
  for p in m:
    print(p)
    for i in range(1, len(str(p))):
      if (p[i:] in m) and (p[:-i] in m):
        b = True
      else:
        b = False

    if b is True:
      f.append(d)
    
print(sum(f))
