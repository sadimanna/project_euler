filename = "pe67.txt"
datafile = open(filename,'r+')
data = []
#Parsing the data
for r in xrange(100):
	datastr = datafile.readline()
	data.append(datastr[0:len(datastr)-1])
for i in xrange(100):
	datastr = data[i]
	data[i] = map(int,datastr.split(' '))
#print data
#Finding the path
pathsum = []
pathsum.append(data[0])
#print pathsum
for i in xrange(99):
	pathsum.append([0]*(i+2))
	for j in xrange(i+1):
		for k in xrange(2):
			temp = pathsum[i][j]+ data[i+1][j+k];
			if temp> pathsum[i+1][j+k]:
				pathsum[i+1][j+k] = temp
greatestSum = max(pathsum[i+1])
print greatestSum
