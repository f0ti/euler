#!/usr/bin/env python3

d = 1
for i in range(1, 101):
  d *= i

print(sum([int(x) for x in list(str(d))]))