#!/usr/bin/env python3

y = 0

while y <= 1000002:
  for a in [x for x in range(0, 10)]:
    for b in [x for x in range(0, 10) if x not in [a]]:
      for c in [x for x in range(0, 10) if x not in [a, b]]:
        for d in [x for x in range(0, 10) if x not in [a, b, c]]:
          for e in [x for x in range(0, 10) if x not in [a, b, c, d]]:
            for f in [x for x in range(0, 10) if x not in [a, b, c, d, e]]:
              for g in [x for x in range(0, 10) if x not in [a, b, c, d, e, f]]:
                for h in [x for x in range(0, 10) if x not in [a, b, c, d, e, f, g]]:
                  for i in [x for x in range(0, 10) if x not in [a, b, c, d, e, f, g, h]]:
                    for j in [x for x in range(0, 10) if x not in [a, b, c, d, e, f, g, h, i]]:
                      y += 1
print(a, b, c, d, e, f, g, h, i, j)