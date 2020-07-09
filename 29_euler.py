#!/usr/bin/env python3

aa = []
for a in range(2, 101):
  for b in range(2, 101):
    aa.append(a**b)

print(len(set(aa)))