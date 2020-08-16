#total m+n moves

def fact(n):
	if n==0 or n==1:
		return 1
	return n*fact(n-1)


if __name__ == "__main__":
	output = 0
	N = 20
	
	print(fact(2*N)//(fact(N)*fact(N)))
