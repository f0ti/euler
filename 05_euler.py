#!/usr/bin/env python3

for i in range(2520, 2**32, 20):
  flag = 0
  for j in range(2, 20):
    if (i%j) == 0:
      flag = 1
    else:
      flag = 0
      break
  if flag:
    print(i)
    break