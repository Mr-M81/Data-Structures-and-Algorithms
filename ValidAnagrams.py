#
# Complete the 'isAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def isAnagram(s, t):
    if len(s) != len(t):
        return 0
    count = {}
    for char in s:
        count[char] = count.get(char,0) + 1
        
    for char in t:
        if char not in count:
            return 0
        else:
            count[char] -= 1
    return 1        
        
    
    
