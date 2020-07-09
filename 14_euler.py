#!/usr/bin/env python3

pp = []
dd = []
for i in range(1, 1000000):
  d = [i]
  while d[-1] != 1:
    if d[-1]%2 == 0:
      d.append(d[-1]/2)
    else:
      d.append(3*d[-1]+1)
  pp.append(len(d))
  dd.append(i)

print(dd[pp.index(max(pp))])