def FourWaySwap(s):
	temp = s[3]
	
	
	s[3] = s[2]
	s[2] = s[1]
	s[1] = s[0]
	s[0] = temp
	return s

print FourWaySwap([1,2,3,4])
