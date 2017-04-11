"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers 
as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hint:
use 'list comprehension'

"""
if __name__ == '__main__':
	numeros = input("Ingrese los numeros separados por coma")
	lista = numeros.split(',')
	respuestas = [i for i in lista if int(i,2)%5==0]
	print(respuestas)