import math, time

def isprime(n):
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return 0
	return 1

if __name__ == '__main__':
	num = 600851475143
	maxprimefactor = 0
	primefactors = []
	factors = []
	prod = 1
	stime = time.time()
	for i in range(3,num//2,2):
		if num%i==0:
			factors.append(i)
			if isprime(i):
				maxprimefactor = i
				primefactors.append(i)
			prod *= i
			if prod == num:
				break

	print(factors)
	print(primefactors)
	print(maxprimefactor)
	print("Time required : %s milliseconds"%((time.time()-stime)*1000))
