def binarySearch(alist, item):
	if len(alist) == 0:
	    return False
	else:
	    midpoint = len(alist)//2
	    if alist[midpoint]==item:
	        return True
	    else:
	        if item<alist[midpoint]:
	            return binarySearch(alist[:midpoint],item)
	        else:
	            return binarySearch(alist[midpoint+1:],item)
			
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

from random import randint

def sel_sort(array):
	for i in range(len(array) - 1):
		m = i
		j = i + 1
		while j < len(array):
			if array[j] < array[m]:
				m = j
			j = j + 1
		array[i], array[m] = array[m], array[i]


a = []
for i in range(10):
	a.append(randint(1, 99))
 
print(a)
sel_sort(a)
print(a)