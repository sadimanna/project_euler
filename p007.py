import numpy as np
import time

if __name__ == '__main__':
	primelist = np.array([2])
	pcount = 1
	pnum = 1
	stime = time.time()
	while pcount!=10001:
		primefound = 0
		pnum+=2
		for i in range(pcount):
			if pnum%primelist[i]==0:
				break
			elif primelist[i]>=np.sqrt(pnum):
				primelist = np.append(primelist,pnum)
				primefound = 1
				break
		if primefound == 1:
			pcount+=1
	print("10001st prime number is %s"%(pnum))
	print("Time taken :: %.3f seconds"%(time.time()-stime))