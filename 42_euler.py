#!/usr/bin/env python3

def triangle(n):
  m = (8*n + 1)**0.5
  return m.is_integer()

with open("p042_words.txt") as f:
  a = f.read()

  aa = a.split('","')
  aa[0]  = aa[0][1:]
  aa[-1] = aa[-1][:-1]

c = 0
for w in aa:
  t = sum([ord(x)-64 for x in w])
  if triangle(t):
    c += 1

print(c)