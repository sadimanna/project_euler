import time

def ispalindrome(num):
	lnum = len(num)
	if lnum % 2 == 0:
		limit = int(lnum/2)
	elif lnum % 2 != 0:
		limit = int((lnum-1)/2)
	for ln in xrange(limit):
		if num[ln]!=num[lnum-ln-1]:
			return 0
	return 1

def dec2bin(num):
	binnum = ''
	while num>0:
		rem = num % 2
		num = num / 2
		binnum = str(rem)+binnum		
	return binnum

def main():
	st = time.time()
	sum_dbpalindrome = 0
	print "Enter upper limit :: "
	lim = int(raw_input())
	for n in xrange(1,lim):
		if ispalindrome(str(n)) and ispalindrome(dec2bin(n)):
			sum_dbpalindrome = sum_dbpalindrome + n
	print "Sum of all double-base palindrome below limit :: "+str(sum_dbpalindrome)+"\n"
	print "Time taken :: "+str(time.time()-st)+" seconds\n"

main()
