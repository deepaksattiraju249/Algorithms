# Anagrams are the permutations of the same characteres

#One layman solution would be count the number of characters  
#if character count of both the strings match then they are Anagrams

def CheckIfAnagrams(s1,s2):
	if len(s1) != len(s2):
		return False

	count_map = dict() 
	for i in xrange(26):
		count_map[chr(i+97)] = 0    # Creating a dictionary of all characters and setting count to 0
	countMapForS1 = count_map
	for ch in s1:
		countMapForS1[ch]+=1;     # Increasing the count of each of those 
	countMapForS2 = count_map
	for ch in s2:
		countMapForS2[ch]+=1;
	for ch in count_map:
		if(countMapForS1[ch] != countMapForS2[ch]):
			return False
	return True

# Order of Time complexity O(N) and order of Space complexity O(c)