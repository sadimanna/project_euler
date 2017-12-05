def proper_divisor(num):
	sumofdiv = 0
	for i in xrange(1,(num/2)+1):
		if(num%i==0):
			sumofdiv = sumofdiv + i
	return sumofdiv

sumamicnum = 0
for j in xrange(1,10001):
	dj = proper_divisor(j)
	if dj != j:
		ddj = proper_divisor(dj)
		if ddj == j:
			sumamicnum = sumamicnum + j

print sumamicnum
