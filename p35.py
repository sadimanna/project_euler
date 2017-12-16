import  time
from math import ceil,sqrt

def isprime(num):
	sqnum = ceil(sqrt(num))
	limit = int(ceil((sqnum-1)/2))+1
	if num == 2 or num == 3:
		return 1
	elif num % 2 == 0:
		return 0
	else:
		for n in xrange(1,limit):
			if num % (2*n+1) == 0:
				return 0
	return 1

def rotate_num(num,nplace,lnum):
	div = 10**(lnum-nplace)
	mul = 10**nplace
	result = (num%div)*mul+(num/div) 
	return result

def iscirc_prime(num):
	lnum = len(str(num))
	for ln in xrange(lnum):
		if not isprime(rotate_num(num,ln,lnum)):
			return 0
	return 1	

def main():
	st = time.time()
	count = 0
	print "Enter upper limit :: "
	lim = int(raw_input())
	for num in xrange(2,lim):
		if iscirc_prime(num):
			#print "Circular prime :",num
			count = count + 1
	print "Number of circular primes below "+str(lim)+" is :: "+str(count)+"\n"
	print "Total time taken :: "+str(time.time()-st)+" seconds\n"

main()
