import math, time

def isprime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n%i==0:
			return 0
	return 1

if __name__ == '__main__':
	lenside = 1
	primeperc = 100
	numprime = 0
	numtot = 1
	stime = time.time()
	while primeperc >= 10 :
		lenside+=2
		val = lenside**2
		lenm1 = lenside - 1

		for i in range(4):
			if isprime(val-i*lenm1):
				#primes.append(val-i*lenm1)
				numprime+=1
		numtot+=4
		primeperc = 100*numprime/numtot
		#print(lenside, primeperc)
	print("Time taken : %s milliseconds"%((time.time()-stime)*1000))
	print(lenside)
