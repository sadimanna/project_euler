fn1 = 1
fn2 = 1
index = 2
nd = 1
while (nd != 1000):
	fn = fn1+fn2
	fn2 = fn1
	fn1 = fn
	index = index + 1
	nd = len(str(fn))
print index
