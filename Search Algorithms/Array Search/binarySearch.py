#sorted array
def BinarySearch(array,item):
	lo = 0
	hi = len(array)
	while lo < hi:
		mid = (lo+hi)/2
		midval = array[mid]
		if midval < item:
			lo = mid+1
		elif midval > item:
			hi = mid
		else:
			return mid
	return -1

print BinarySearch([1,2,3,4,5,6,7,8,9], 5)