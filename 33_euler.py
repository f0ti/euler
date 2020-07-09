#!/usr/bin/env python3

aa = []
b = 1

for i in range(10, 101):
  for j in range(10, 101):
    if i%10 == 0 or j %10 == 0:
      continue
    val = i/j
    num = list(str(i))
    den = list(str(j))

    for x in num:
      for y in den:
        if int(x)/int(y) == val:
          aa.append((x, y))
          b *= int(y)

print(aa)
print(b)