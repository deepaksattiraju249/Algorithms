# Without using extra data structures

def UniqueCharacters(s):
    checker = 0
    for character in s:
        val = ord(character) - ord('a')
        bitUpdate = 2**val
        if(checker & bitUpdate != 0):
            return False
        checker |= 2**val

    return True

print UniqueCharacters("avsc")
