#!/usr/bin/env python3

gg = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
      11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
      20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"}

w = ""

for i in range(1, 1000):
  s = ""
  if i > 20 and i < 100:
    s += gg[i-i%10] + gg[i%10]
  elif i%100 == 0:
    s += gg[i//100] + gg[100]
  elif i > 100 and i%100 != 0:
    if i%100 < 20:
      s += gg[i//100] + "hundredand" + gg[i%100]
    else:
      s += gg[i//100] + "hundredand" + gg[i%100-i%10] + gg[i%10]
  else:
    s += gg[i]
  
  w += s

  print("{}: {}".format(i, s))

w += "onethousand"
print(w)

print(len(w))