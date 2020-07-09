#!/usr/bin/env python3

f1 = 1
f2 = 1

a = [f1, f2]
i = 2
while len(str(a[-1])) < 1000:
  i = i+1
  a.append(a[-1] + a[-2])

print(a.index(a[-1]))
print(i)