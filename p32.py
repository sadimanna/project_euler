if __name__ == '__main__':
	output = 0
	prods = []
	for i in range(1,5000):
		for j in range(1,10000//i):
			prod = i*j

			listi = list(str(i))
			listj = list(str(j))
			listp = list(str(prod))

			listf = listi+listj+listp
			allin = False
			#print(listf,list(set(listf)))
			if len(set(listf)) == len(listf) and '0' not in listf:
				allin = True
				for k in range(1,10):
					if str(k) in list(set(listf)):
						allin*=True
					else:
						allin*=False
			if allin == True:
				if prod not in prods:
					print(i,j,prod)
					prods.append(prod)
					output += prod

	print(output)