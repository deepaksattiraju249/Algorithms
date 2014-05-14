#One more way to solve is sort the strings
# and compare the strings

def CheckAnagram(s1,s2):
	if len(s1) != len(s2):
		return False

	s1 = list(s1).sort()
	s2 = list(s2).sort()
	if(s1 == s2):
		return True
	else:
		return False

#Order of Time Complexity O(NlogN)
#Order of Space Complexity O(N)
