import time
from math import sqrt

def is_triangular(num):
	#n2+n-2*num = 0
	n = (-1 + sqrt(1+4*2*num))/2
	if n==int(n):
		return 1
	else:
		return 0

def main():
	st = time.time()
	count = 0
	filename = "p042_words.txt"
	file = open(filename,'r+')
	words = file.read().replace('"','').split(',')
	for w in words:
		value = 0		
		lenw = len(w)
		for i in xrange(lenw):
			value = value + (ord(w[i])-64)
		if is_triangular(value):
			count = count+1
	print "Number of triangular words :: "+str(count)
	print "Time taken :: "+str(time.time()-st)+" seconds\n"

main()
