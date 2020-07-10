#!/usr/bin/env python3

import math

# Binomial coeff 4ever

def find_bin_coeff(n, k):
  return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print(int(find_bin_coeff(40, 20)))