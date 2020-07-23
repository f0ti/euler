#!/usr/bin/env python3

# The idea is basically the same as writing
# the number as product of prime numbers

n = 600851475143

for i in range(2, 10000):
  while n%i == 0:
    n //= i
    if n == 1 or n == i:
      print(i)
      break