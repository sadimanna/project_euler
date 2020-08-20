import time

def square_and_add_digits(n):
	digits = list(map(int,list(str(n))))
	digits = [d*d for d in digits]
	return sum(digits)

if __name__ == '__main__':
	MAXN = 10000000
	linked_dict = {}
	count = 0
	stime = time.time()
	for n in range(1,MAXN+1):

		intermediates = []

		sqrdnadded = square_and_add_digits(n)
		intermediates.append(sqrdnadded)
		
		if n<=10000:
			linked_dict[n] = sqrdnadded
		
		#print("%s -> %s"%(n,sqrdnadded),end=" ")
		
		while sqrdnadded != 1 and sqrdnadded != 89:
			sqrdnadded2 = square_and_add_digits(sqrdnadded)
			intermediates += [sqrdnadded2]

			if n<=10000:
				linked_dict[n] = sqrdnadded2
			if sqrdnadded <= 10000:
				linked_dict[sqrdnadded] = sqrdnadded2
			
			sqrdnadded = sqrdnadded2
			#print("-> %s"%(sqrdnadded),end=' ')
		#print()

		#print(intermediates)
		for intm in intermediates:
			if intm <= 10000:
				linked_dict[intm] = sqrdnadded

		if sqrdnadded == 89:
			count +=1

	#print(linked_dict)
	print("Time taken :: %s seconds"%(time.time()-stime))
	print(count)

