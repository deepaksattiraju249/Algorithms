def mergeSort(array):
	if len(array)< 2:
		return array
	result = []
	mid = int(len(array)/2)
	L = mergeSort(array[:mid])
	R = mergeSort(array[mid:])
	i = 0
	j = 0
	while i < len(L) and j <len(R):
		if(L[i] <= R[j]):
			result.append(L[i])
			i+= 1
		else:
			result.append(R[j])
			j+=1
	while i < len(L):
		result.append(L[i])
		i+=1

	while j < len(R):
		result.append(R[j])
		j+=1
	return result


array = [5,4,3,2,1]
array = mergeSort(array)
print array