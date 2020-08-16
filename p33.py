numerator = []
denominator = []

cancellednum = []
cancelledden = []

for n in range(10,100):
	for d in range(10,100):
		num = list(str(n))
		den = list(str(d))
		if num[-1]!='0' and den[-1]!='0' and ((n/d)<1) and n!=d:
			intersection = []
			for nm in num:
				if nm in den and nm not in intersection:
					intersection.append(nm)
			if len(intersection)==0:
				continue
			for inter in intersection:
				num.remove(inter)
				den.remove(inter)
			#print(num, den)
			if (''.join(num) != '' or ''.join(den)!='') and ''.join(num) != '0' and ''.join(den)!='0':
				if (n/d) < 1 and (n/d)==int(''.join(num))/int(''.join(den)):
					numerator.append(n)
					denominator.append(d)
					cancellednum.append(int(''.join(num)))
					cancelledden.append(int(''.join(den)))

print(numerator)
print(denominator)
print(cancellednum)
print(cancelledden)





