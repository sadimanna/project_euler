from math import floor, log10, sqrt

if __name__ == '__main__':
	p099_file = open('p099_base_exp.txt','r')
	base_exp = list(map(lambda x:x.rstrip('\n'),p099_file.readlines()))
	base = []
	exp = []
	for be in base_exp:
		b,e = be.split(',')
		base.append(int(b))
		exp.append(int(e))
	
	maxnum = 0
	maxnumind = 0
	for i in range(1,1000+1):
		num = exp[i-1]*log10(base[i-1])
		#print(num)
		if num>maxnum:
			maxnum = num
			#print(base[i],exp[i],numdigs)
			maxnumind = i

	print(maxnumind)