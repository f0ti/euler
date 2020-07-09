#!/usr/bin/env python3

a = sum(list(range(1, 101))) ** 2
b = sum([x**2 for x in list(range(1, 101))])

print(a-b)
