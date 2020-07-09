#!/usr/bin/env python3

f = open('p022_names.txt', 'r')
a = f.read()

aa = a.split('","')
aa[0]  = aa[0][1:]
aa[-1] = aa[-1][:-1]

aa.sort()

s = 0

for i, word in enumerate(aa, 1):
  ss = 0
  for c in word:
    ss += ord(c.lower())-96
  s += ss*i

  print(i, word, ss*i)

print(s)