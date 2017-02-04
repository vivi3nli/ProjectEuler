def Sum():
	i = 1
	Sum = 0
	n = [1,2]
	for  n[i] in range(4000000):
		if n[i] % 2 == 0:
			Sum += n[i]
		n.append(n[i] + n[i - 1])
		i += 1

print Sum()

#how about doing it recursively
