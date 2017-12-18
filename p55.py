import time

def reversenum(num):
	rnum = 0
	while num>0:
		rem = num%10
		num = num/10
		rnum = rnum*10+rem
	return rnum

def ispalindrome(num):
	num = str(num)
	ln = len(num)
	if ln % 2 == 0:
		lim = ln/2
	else:
		lim = (ln+1)/2
	for j in xrange(lim):
		if num[j] != num[ln-j-1]:
			return 0
	return 1

st = time.time()
nIter = 50
limit = 10000
count = 0
for n in xrange(1,limit):
	ip = 0
	lnum = n
	for i in xrange(nIter):
		lnum = lnum + reversenum(lnum)
		if ispalindrome(lnum):
			ip = 1	
			break
	if ip == 0:
		count = count + 1

print "Number of Lychrel numbers :: "+str(count)
print "Time taken :: "+str(time.time()-st)+" seconds\n"





























#print reversenum(123456789)
