#!/usr/bin/env python3

def prime_factors(n):
  i = 2
  factors = {}
  while n > 1:
    if n % i:
      i += 1
    else:
      n //= i
      if i not in factors:
        factors[i] = 1
      else:
        factors[i] += 1
  return factors

def nr_divisors(n):

  d = prime_factors(n)
  nr = 1

  for k in d:
    nr *= d[k] + 1

  return nr

def main():
  for i in range(1, 2**16):
    number = sum (j for j in range(1, i+1))
    if nr_divisors(number) > 500:
      print(number)

if __name__ == "__main__":
  main()