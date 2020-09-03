import time
if __name__ == "__main__":
	N = 1000
	maxrecurr = 0
	maxrecurr_d = None
	stime = time.time()
	for d in range(2,N):
		decimalval = '.'
		decimalcycle = ''
		num = 1
		recurr = 0
		cycle = 0
		num_states = []
		
		while(cycle==0):
			num_states.append(num)
			num*=10
			dig = str(num//d)
			num = num%d
			decimalval += dig
			if num==0:
				cycle=1
			if num!=0:
				if num in num_states:
					ind = 0
					for i in range(len(num_states)-1,0,-1):
						if num_states[i]==num:
							ind = i
							break
					recurr = len(num_states) - ind
					cycle = 1

		if recurr > maxrecurr:
			maxrecurr = recurr
			maxrecurr_d = d
		#print('1/%d = 0%s -> %d'%(d,decimalval,recurr))
	print("Time taken : %.3f seconds."%(time.time()-stime))
	print("Maximum Recurring decimal is of length %d for d = %d"%(maxrecurr,maxrecurr_d))