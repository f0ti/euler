#!/usr/bin/env python3

import math

s = 0
for x in range(3, 2**16):
  if sum([math.factorial(int(f)) for f in str(x)]) == x:
    s += x

print(s)