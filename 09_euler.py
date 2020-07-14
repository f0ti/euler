#!/usr/bin/env python3

for c in range(1, 1000):
  for b in range(1, c):
    for a in range(1, b):
      if (a*a + b*b == c*c) and (a+b+c == 1000):
        print(a*b*c)
        break