"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

"""

def main():
    pass

if __name__ == '__main__':
	lista = []
	for x in range(2000,3200):
		if x%7==0 and x%5!=0:
			lista.append(x)
	print(lista)

  
    	