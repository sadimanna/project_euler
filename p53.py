import math, time

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)

if __name__ == '__main__':
	MAXN = 100
	MINN = 1
	count = 0

	FACTS = [1]
	for n in range(1,MAXN+1):
		FACTS.append(fact(n))

	#print(FACTS)

	for n in range(1,MAXN+1):
		MINR = 0
		MAXR = n//2 + 1
		for r in range(MINR,MAXR):
			val = 1
			for i in range(n-r+1,n+1):
				val*=i
			val/=FACTS[r]
			#print('%sC%s and %sC%s: %s'%(n,r,n,n-r,val))
			if val > 1000000:
				if n%2==0 and r==n//2:
					count+=1
				else:
					count+=2
		#print('----------------------------')

	print(count)
