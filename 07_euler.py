#!/usr/bin/env python3

m = []
i = 1

while len(m) < 10001:
  i += 1
  not_prime = 0
  for j in range(2, i):
    if i%j == 0:
      not_prime = 1
      break
  if not_prime == 0:
    m.append(i)
  print(len(m))
print(m[-1])