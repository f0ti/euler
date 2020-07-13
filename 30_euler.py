#!/usr/bin/env python3

s = 0

for i in range(2**25):
  d = [int(x) for x in list(str(i))]
  pp = [x**5 for x in d]
  if sum(pp) == i:
    s += i

print(s-1)