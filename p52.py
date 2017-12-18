import time

def is_samedig(n,mn):
	ln = len(str(n))
	lmn = len(str(mn))
	ndig = set(list(str(n)))
	mndig = set(list(str(mn)))
	if ndig == mndig:
		return 1
	return 0

st = time.time()

for n in xrange(1,10000000):
	count = 0
	for m in xrange(2,7):
		if is_samedig(n,m*n):
			count = count + 1
	if count == 5:
		num = n
		break

print "Smallest Positve Integer :: "+str(num)
print "Time taken :: "+str(time.time()-st)+" seconds\n"
