import time
from math import sqrt

def is_pentagonal(tnum):
	n = (1 + sqrt(1 + 4*3*2*tnum))/(2*3)
	if n == int(n):
		return 1
	else:
		return 0

st = time.time()
D = 0
minD = 0
start = 0
pent_num = [n*(3*n-1)/2 for n in xrange(1,10001)]
for j in xrange(10000):
	Pj = pent_num[j]
	for k in xrange(start,10000):
		Pk = pent_num[k]
		if is_pentagonal(Pj+Pk) and is_pentagonal(abs(Pj-Pk)):
			D = abs(Pk-Pj)
			if D < minD:
				minD = D
	start = start + 1	

print "Value of D :: "+str(D)
print "Time taken :: "+str(time.time()-st)+" seconds\n"
