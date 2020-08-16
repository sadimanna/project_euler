def fifthpow(n):
	return n*n*n*n*n

if __name__ == '__main__':

	output = 0

	for n in range(2, 1000000):
		#print(sum(list(map(fifthppow,list(map(int,list(str(n))))))))
		if sum(list(map(fifthpow,list(map(int,list(str(n))))))) == n:
			print(n)
			output+=n

	print(output)