import time

def calcpow(b,e):
	result = 1
	for i in xrange(e):
		result = result*b
	return result

st = time.time()

self_pow_sum = 0

print "Enter range :: "
N = int(raw_input())

for i in xrange(1,N+1):
	self_pow_sum = self_pow_sum + calcpow(i,i)

result = self_pow_sum % 10000000000

print "Last ten digits :: "+str(result)
print "Time taken :: "+str(time.time()-st)+" seconds\n"
