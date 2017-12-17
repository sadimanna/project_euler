import time

def factorial(num):
	fact = 1
	for n in xrange(1,num+1):
		fact = fact * n
	return fact

def sum_fact_dig(num):
	sumfd = 0
	lnum = len(str(num))
	for ln in xrange(lnum):
		sumfd = sumfd + factorial(num % 10)
		num = num / 10
	return sumfd

def curious_num(num):
	if num == sum_fact_dig(num):
		return 1
	return 0

def main():
	st = time.time()
	sumcn = 0
	for i in xrange(3,10000000):
		if curious_num(i):
			sumcn = sumcn + i
	print "Sum of all curious number :: "+str(sumcn)+"\n"
	print "Time taken :: "+str(time.time()-st)+" seconds\n"

main()
