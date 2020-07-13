#!/usr/bin/env python3

a, b, s = 0, 1, 0
fib = [a, b]

while fib[-1] < 4000000:

  fib.append(a+b)
  if (a+b)%2  == 0:
    s += (a+b)
  
  a = fib[-2]
  b = fib[-1]

print(s)