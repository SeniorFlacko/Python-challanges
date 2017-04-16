"""
Given an array of equal-length strings, check if it is possible to rearrange 
the strings in such a way that after the rearrangement the strings at consecutive 
positions would differ by exactly one character.

Hint
For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false;
For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

"""
def isadjacent(palabra1,palabra2):
	count=0
	n=len(palabra1)
	for i in range(n):
		if palabra1[i] is not palabra2[i]:
			count+=1
		if count>1:
			return False
return True if count is 1 else False

def stringsRearrangement(inputArray):
    

if __name__ == '__main__':
	lista = ["aba","bbb","bab"]
	stringsRearrangement(lista)
	