#Bisection Search

def bisection(array, item):
	length = len(array)
	mid = length/2 
	if length==0:
		return False
	if length == 1:
		return array[0] == item
	if array[mid] == item:
		return True
	else:
		print array
		print array[:mid]
		print array[mid+1:]
		return bisection(array[:mid],item) or bisection(array[mid+1:],item)


print bisection([1,2,3,45,6,23], 1)