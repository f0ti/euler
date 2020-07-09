#!/usr/bin/env python3

mx = []
for i in range(101, 1000):
  for j in range(101, 1000):
    m = str(i*j)
    if len(m)%2 == 0:
      if m[0:(len(m)//2)] == m[(len(m)//2):][::-1]:
        mx.append(m) 
        print(m, "=>", i, " ", j)
    else:
      if m[0:(len(m)//2)] == m[0:(len(m)//2)+1][::-1]:
        mx.append(m)
        print(m, "=>", i, " ", j)

print(max(mx))
