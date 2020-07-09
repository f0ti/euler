#!/usr/bin/env python3

for i in range(2, 2**20):
  x  = list(str(i))
  x2 = list(str(i*2))
  x3 = list(str(i*3))
  x4 = list(str(i*4))
  x5 = list(str(i*5))
  x6 = list(str(i*6))
  x.sort()
  x2.sort()
  x3.sort()
  x4.sort()
  x5.sort()
  x6.sort()

  if x2 == x and x3 == x and x4 == x and x5 == x and x6 == x:
    print(i)