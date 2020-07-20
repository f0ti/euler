#!/usr/bin/env python3

def pentagonal(n):
  i = 1
  while 1:
    a = (3*i*i - i)//2
    i += 1
    if (a >= n):
      break
  return (a == n)

aa = []
j = 0
while 1:
  j += 1
  p = j*(3*j-1)//2
  print(j)
  for g in aa:
    if pentagonal(p-g) and pentagonal(p+g):
      print(p, g)
      print(abs(p-g))
      break
  aa.append(p)