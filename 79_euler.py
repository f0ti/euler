#!/usr/bin/env python3

with open("p079_keylog.txt") as f:
  c = [line.rstrip() for line in f]

c = list(set(c))

print(c)

for n in c:
  print("Pas {} vijne {}".format(n[0], n[1:]))
  print("Pas {} vijne {}".format(n[1], n[2:]))
