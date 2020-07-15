#!/usr/bin/env python3

s = 0

for i in range(1, 1000000):
  b = str(bin(i))[2:]
  d = str(i)
  if b == b[::-1] and d == d[::-1]:
    s += i
    print(i, ": ", b)

print(s)