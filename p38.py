if __name__ == '__main__':
	largestn = 1
	largestmults = []
	for n in range(1,10000):
		listd = []
		mults= []
		for i in range(1,10):
			listi = list(str(n*i))
			if '0' in listi or len(set(listd+listi))!=len(listd+listi):
				break
			else:
				listd += listi
				mults.append(i)
		#print(listd, mults)
		if ''.join(sorted(listd))=='123456789':
			if largestn < int(''.join(listd)):
				largestn = int(''.join(listd))
				print(largestn, n,mults)
	print(largestn)