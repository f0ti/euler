#!/usr/bin/env python3

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p).

w = 0

for a in range(0, 201):
  for b in range(0, 101):
    for c in range(0, 41):
      for d in range(0, 21):
        for e in range(0, 11):
          for f in range(0, 5):
            for g in range(0, 3):
              if a*1+b*2+c*5+d*10+e*20+f*50+g*1 == 200:
                w += 1
print(w+1)