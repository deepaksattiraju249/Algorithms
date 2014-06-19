def selectionSort(array):
	length = len(array)
	for i in range(length):
		minimum = array[i]
		index = i
		for j in range(i,length):
			if array[j] < minimum:
				minimum = array[j]
				index = j
		array[index] = array[i]
		array[i] = minimum
	return array


print selectionSort([5,4,3,2,1])

