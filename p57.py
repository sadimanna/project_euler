def one_plus_fraction(num,den):
	return num+den, den

def one_over_fraction(num,den):
	return den, num

if __name__ == '__main__':
	fracnum = 1
	fracden = 2
	MAXN = 1000
	count = 0
	#Add - Inverse - Add
	for n in range(1,MAXN+1):
		if n==1:
			fracnum, fracden = one_plus_fraction(fracnum,fracden)
			#continue
		else:
			fracnum, fracden = one_plus_fraction(fracnum,fracden)
			fracnum, fracden = one_over_fraction(fracnum,fracden)
			fracnum, fracden = one_plus_fraction(fracnum,fracden)
		if len(str(fracnum))>len(str(fracden)):
			count += 1
		#print("%s/%s"%(fracnum,fracden))
		#print("%.10f"%(fracnum/fracden))
	print(count)