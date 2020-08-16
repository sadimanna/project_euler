# GOLDBACH'S OTHER CONJECTURE
from math import sqrt, ceil
def isprime(n):
	for i in range(2,ceil(sqrt(n))+1):
		if n%i==0:
			return 0
	return 1

if __name__ == '__main__':
	found = 0
	n = 35
	while(found == 0):
		i = 0
		satisfied = 0
		while not satisfied:
			i+=1
			temp = n - 2*i*i
			
			if temp < 0:
				if not isprime(n):
					found = 1
					break
				else:
					satisfied = isprime(n)
					temp = n
					i = 0
			else:
				satisfied = isprime(temp)
			
			if satisfied:
				print("%s = %s + 2X(%s)^2"%(n,temp,i))
				break
		if found==0:
			n+=2
	print(n)