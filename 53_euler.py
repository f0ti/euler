#!/usr/bin/env python3

import math

many = 0
for n in range(1, 101):
  for r in range(1, n+1):
    x = math.factorial(n)//math.factorial(r)*math.factorial(n-r)
    if x > 1000000:
      print(x)
      many += 1

print(many)