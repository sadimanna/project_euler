if __name__ == '__main__':
	keylogfile = open('p079_keylog.txt','r')
	keylogs = list(map(int,list(map(lambda s: s.strip(), keylogfile.readlines()))))
	passcode = []
	print(keylogs)
	for key in keylogs:
		digits = list(str(key))
		if passcode==[]:
			passcode+=digits
		else:
			for i in range(3):
				d = digits[i]
				if d in passcode:
					for j in range(i):
						indj = passcode.index(digits[j])
						dind = passcode.index(d)
						if indj > dind:
							passcode[indj],passcode[dind] = passcode[dind],passcode[indj]
				else:
					if i!=0:
						passcode.insert(passcode.index(digits[i-1])+1,d)
					else:
						passcode.append(d)
		#print(passcode)
	print(''.join(passcode))