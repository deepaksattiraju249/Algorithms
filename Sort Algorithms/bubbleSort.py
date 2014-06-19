def BubbleSort(array):
	length = len(array)
	for i in range(length):
		for j in range (length-1 , i-1,-1):
			if array[j] < array[j-1]:
				(array[j],array[j-1]) = (array[j-1],array[j])
	return array

print BubbleSort([5,4,3,2,1])