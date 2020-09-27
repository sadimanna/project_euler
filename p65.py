import time

def inte_plus_fraction(num,den,inte):
	return num+den*inte, den

def one_over_fraction(num,den=1):
	return den, num

if __name__ == '__main__':
	liste = [2]
	for i in range(1,1+100//3):
		liste += [1,2*i,1]
	print(liste)
	fracnum = (liste[-1],1)
	for i in range(99,0,-1):
		fracnum = one_over_fraction(fracnum[0],fracnum[1])
		#print()
		fracnum = inte_plus_fraction(fracnum[0],fracnum[1],liste[i-1])
	print(sum(list(map(int,list(str(fracnum[0]))))))
