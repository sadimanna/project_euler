import math
def isprime(n):
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return 0
	return 1

if __name__ == '__main__':
	primesum = 0
	primelist = []
	sumlist = 0
	limit = 1000000
	for i in range(2,limit):
		if isprime(i):
			primelist.append(i)
			sumlist+=i
		if sumlist>limit:
			break

	#print(sumlist)
	#print(primelist)

	positional_sum = []
	for i in range(len(primelist)):
		positional_sum.append(sum(primelist[i:]))

	#print(positional_sum)
	output = 0
	maxsum = 0
	primelen = 0
	for i in range(len(primelist)):
		for j in range(len(positional_sum)):
			if (len(positional_sum)-j)>primelen and positional_sum[j]>maxsum and positional_sum[j]<limit and isprime(positional_sum[j]):
				output = positional_sum[j]
				primelen = len(primelist)-1-j
		m = positional_sum[-1]
		positional_sum = positional_sum[:-1]
		positional_sum = [p-m for p in positional_sum]
		#print(positional_sum)

	print(output)

	