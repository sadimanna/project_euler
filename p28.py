# -*- coding: utf-8 -*-

import numpy as np
import time

#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13

#   5X5 matrix, top right is 5^2. top left is 25-(5-1). bottom left is 25-(5-1)-(5-1). bottom right is 25-(5-1)-(5-1)-(5-1)
#   After these elements are accessed, the matrix reduces to 3X3 matrix, follow similar approach

n = 1001
sum = 0
temp = 0
start = time.time()
while n>1:
    temp = n**2
    for i in range(4):
        sum += temp-(3-i)*(n-1)
    n = n - 2
sum+=1
print("Total time : ",time.time()-start,"seconds.")

print(sum)

