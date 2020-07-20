#!/usr/bin/env python3

nr_m, m = 0, 0

for i in range(2, 1000):
  s = str(1/i)[2:]
  for j in range(2, 20):
    if s[:j] not in s[j:]:
      if j > m:
        m = j
        nr_m = i

print(nr_m)
print(m)