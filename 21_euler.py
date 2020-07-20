#!/usr/bin/env python3

a = {}

for i in range(1, 10001):
  s = 0
  for j in range(1, i//2+2):
    if i % j == 0:
      s += j
  a[i] = s

l = set()
for k, v in a.items():
  try:
    if k == a[v] and k != v:
      l.add(k)
      l.add(v)
  except:
    continue

print(l)
print(sum(l))