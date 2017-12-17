import time
from math import sqrt
def ispentagonal(tnum):
	n = (1 + sqrt(1 + 4*2*tnum))/(2*2)
	if n == int(n):
		return 1
	else:
		return 0
	
def ishexagonal(tnum):
	n = (1 + sqrt(1 + 4*3*2*tnum))/(2*3)
	if n == int(n):
		return 1
	else:
		return 0
	
def triangular(num):
	return int(num*(num+1)/2)

def main():
	st = time.time()
	found = 0
	num = 286
	while(found == 0):
		triangularnum = triangular(num)
		if ispentagonal(triangularnum) and ishexagonal(triangularnum):
			found = 1
		else:
			num=num+1
	print "Number ::",triangularnum
	print "Time taken :: "+str(time.time()-st)+" seconds\n"

main()

#3n2-n-2*tnum = 0
#2n2-n-tnum = 0
