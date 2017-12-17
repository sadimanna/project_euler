import time

def main():
	st = time.time()
	maxp = None	
	maxcount = 0
	print "Enter limit of p :: "
	p = int(raw_input())
	peri = {}
	sides = {}
	loop_lim = int(p/2)+1
	for a in xrange(1,loop_lim):
		for b in xrange(1,loop_lim):
			for c in xrange(1,loop_lim):
				if a**2+b**2==c**2:
					pm = a+b+c
					try:
						if a not in sides[pm] and b not in sides[pm] and c not in sides[pm]:
							peri[pm] = peri[pm] + 1
					except:
						sides[pm] = set([a,b,c])
						peri[pm] = 1
					sides[pm].add(a)
					sides[pm].add(b)
					sides[pm].add(c)
	for pm in peri.keys():
		if peri[pm]>maxcount:
			maxcount = peri[pm]
			maxp = pm
	print "Maximum number of solutions for :: "+str(maxp)
	print "Maximum number of solutions :: "+str(maxcount)
	print "Time taken :: "+str(time.time()-st)+" seconds\n"

main()
