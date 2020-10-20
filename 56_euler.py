m = 0
for x in range(50, 100):
	for y in range(50, 100):
		if (s := sum([int(x) for x in list(str(x**y))])) > m:
			m = s
print(m)

