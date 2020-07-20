#!/usr/bin/env python3

# can use perfect test instead

t = [n*(n+1)//2 for n in range(285, 500000)]
p = [n*(3*n-1)//2 for n in range(165, 500000)]
h = [n*(2*n-1) for n in range(144, 500000)]

for j, i in enumerate(t):
  if i in p and i in h:
    print(i)
    break
