import time
import numpy as np

def num_with_sqr_lt_n(n):
	while not np.sqrt(n).is_integer():
		n-=1
	return int(np.sqrt(n))

def process(n, state):
	num = state[0]
	sub = state[1]
	den = n - sub**2
	if den%num==0:
		den = den/num
	sub = -1*sub
	num = np.sqrt(n)+sub
	#print('\n',den,sub,num,'\n')
	a = 0
	while num/den > 1:
		a += 1
		sub -= den
		num -= den
		#print('\n',den,sub,num,'\n')
	return (den,sub,a)

def print_fn(n,state):
	print('\n    '+str(int(state[0])))
	print('-----------')
	print(u'\u221A'+str(n)+' + ('+str(int(state[1]))+')\n') 

if __name__ == '__main__':
	N = 13
	odd_count = 0
	stime = time.time()
	for n in range(2,N+1):
		print("\nN = %d "%(n))
		a0 = num_with_sqr_lt_n(n)
		a = [a0]
		if a0 == np.sqrt(n):
			#print(a)
			continue
		states = [(1,-1*a0)]
		#print_fn(n,states[0])
		currState = None
		while True:
			if currState == None:
				currState = states[-1]
			currState = process(n,currState)
			a.append(currState[-1])
			currState = (currState[0],currState[1])
			if currState in states:
				break
			states.append(currState)
			#print_fn(n,currState)
		if len(a)%2==0:
			odd_count+=1
		print('['+str(a[0])+';('+','.join(list(map(str,a[1:])))+')]')
	print("\nNumber of Continues Fractions having Odd Period : %d"%odd_count)
	print("\nTotal Time Taken : %.3f seconds\n"%(time.time()-stime))