import time
import sympy as sp

if __name__ == '__main__':
	stime = time.time()
	denominations = [1,2,5,10,20,50,100,200]

	maxpowers = [200//d for d in denominations]

	x = sp.symbols('x')

	expr_dict = {}
	for i in range(len(denominations)):
		power = maxpowers[i]
		expr_dict[denominations[i]] = 1
		for p in range(1,power+1):
			expr_dict[denominations[i]] += x**(p*denominations[i])

	GF = 1
	for i in range(len(denominations)):
		GF *= expr_dict[list(expr_dict.keys())[i]]
	GF = sp.expand(GF)

	print("Number of ways = Co-efficient of x**200 in the Generating Function : %d"%(GF.coeff(x,200)))
	print("Time Taken : %.3f seconds"%(time.time()-stime))

