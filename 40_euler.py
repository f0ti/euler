#!/usr/bin/env python3

d = ""
s = 1

while len(d) <= 1000000:
  d = "".join(str(i) for i in range(1, 1000000))

for j in range(7):
  s *= int(d[10**j-1])

print(s)