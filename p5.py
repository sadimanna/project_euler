import numpy as np
import time

def main():
	allnum = np.array(list(range(2,21)))
	fact = 2
	prod = 1

	while not np.all(allnum==1):
		nextfact = 1
		for i in range(len(allnum)):
			if allnum[i]%fact==0:
				allnum[i] = allnum[i]//fact
				nextfact = 0
		#print(allnum,np.all(allnum==1))
		if nextfact:
			fact+=1
		else:
			prod *=fact

	print(prod)

main()