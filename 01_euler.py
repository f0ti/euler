#!/usr/bin/env python3

s = 0
for i in range(0, 1000):
  if i%3 == 0 or i%5 == 0:
    s += i

print(s)