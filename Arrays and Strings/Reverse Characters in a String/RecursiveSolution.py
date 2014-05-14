# Converts the string to list and returns a String
# after Reversing the elements on the string
def reverseString(s):
    ConvList = list(s)
    lastChar = ConvList[-1]
    ConvList = rev(ConvList[:-1],0)
    ConvList.append(lastChar)
    return "".join(ConvList)

#Takes in input as a list and recursively swaps the elements
def rev(s, i):
    if(i == len(s)/2):
        return s
    else:
        temp = s[-i-1]
        s[-i-1] = s [i]
        s[i] = temp
        return rev(s, i+1)

print reverseString("deepak#")
