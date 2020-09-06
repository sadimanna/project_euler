import time
import numpy as np

def isleapyear(year):
	if year%4==0:
		if year%100==0:
			if year%400==0:
				return True
			elif year%400!=0:
				return False
		else:
			return True
	return False

if __name__ == '__main__':
	num_sunday = 0
	year = 1900
	monthsdsnonleap = {'January':31,'February':28,'March':31,
			    	   'April':30,'May':31,'June':30,
			    	   'July':31,'August':31,'September':30,
			    	   'October':31,'November':30,'December':31}
	monthsdsleap = {'January':31,'February':29,'March':31,
			    	'April':30,'May':31,'June':30,
			    	'July':31,'August':31,'September':30,
			    	'October':31,'November':30,'December':31}
	stime = time.time()
	numdays = 365
	firstofeachmonth = [1]
	monthsds = monthsdsnonleap
	months = list(monthsds.keys())
	for m in months[:-1]:
		firstofeachmonth.append((firstofeachmonth[-1]+monthsds[m]%7)%7)
	firstofeachmonth = dict(zip(months,firstofeachmonth))
	#print(firstofeachmonth)
	firstofeachmonth = [(firstofeachmonth['December']+monthsds['December']%7)%7]
	#print(firstofeachmonth)
	year = 1901
	while year<=2000:
		#print(isleapyear(year),year)
		if isleapyear(year):
			monthsds = monthsdsleap
		else:
			monthsds = monthsdsnonleap
		for m in months[:-1]:
			firstofeachmonth.append((firstofeachmonth[-1]+monthsds[m]%7)%7)
			#print(monthsds[m],firstofeachmonth)
		firstofeachmonth = dict(zip(months,firstofeachmonth))
		
		#print(np.count_nonzero(np.array(list(firstofeachmonth.values()))==0))
		num_sunday += np.count_nonzero(np.array(list(firstofeachmonth.values()))==0)

		year +=1
		firstofeachmonth = [(firstofeachmonth['December']+monthsds['December']%7)%7]
		
	print(num_sunday)
	print("Time taken :: %.3f seconds"%(time.time()-stime))