#using inbuilt Function assuming last character to be null
#ignoring the last character

def reverseString(s):
    return s[-2::-1] + s[-1]
    
