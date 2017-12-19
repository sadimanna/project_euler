import time
from decimal import *
getcontext().prec = 102

st = time.time()
total = 0
for n in xrange(1,101):
	sqrtn = str(Decimal(n).sqrt())
	#print len(sqrtn)
	#print sqrtn
	if int(float(sqrtn))!=float(sqrtn):
		sqrtn = sqrtn.replace('.','')
		decimal_dig = sqrtn[:100]
		#print len(decimal_dig)
		sum_dig = sum(int(i) for i in decimal_dig)
		total = total + sum_dig

print "Result ::",total
print "Time taken :: "+str(time.time()-st)+" seconds\n"
		
	
