def insertionSort(array):
	length = len(array)
	for i in range(1,length):
		j = i
		while  j > 0 and array[j-1] > array[j]:
			temp = array[j]
			array[j] = array[j-1]
			array[j-1] = temp
			j -=1 


	return array

print insertionSort([5,4,3,2,1])