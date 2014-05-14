#Checking if s2 is the rotated version of s1
def isRotation(s1,s2):
    if(len(s1) != len(s2)):
        return False
    s = s2 + s2
    if( s1 in s2):
        return True
    return False
