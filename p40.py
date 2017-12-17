import time
st = time.time()
fraction = "0."
places_of_digits = [1,10,100,1000,10000,100000,1000000]
pod = 0
d_index = places_of_digits[pod]

result = 1
present_num = 0
lenfp = 0
done = 0
while(lenfp <= places_of_digits[-1]): 
	present_num = present_num + 1
	fraction = fraction + str(present_num)
	lenpn = len(str(present_num))
	if lenpn >= 1:
		for i in xrange(1,lenpn+1):
			lenfp = lenfp + 1
			if lenfp == d_index:
				result = result * int(str(present_num)[i-1])
				pod = pod + 1
				if pod < len(places_of_digits):
					d_index = places_of_digits[pod]

#print "Fraction :: "+str(fraction)
print "Result :: "+str(result)
print "Time taken :: "+str(time.time()-st)+" seconds\n"
