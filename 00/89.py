	res = [0]
	for i in range(1, 2**n):
		res.append(res[-1] ^ (i & -i))
	return res