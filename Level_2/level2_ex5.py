"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hint: 
search isdigit & isalpha


"""
digits  = 0
letters = 0
if __name__ == '__main__':
	cadena = input("Ingrese una cadena: ")
	for c in cadena:
		if c.isdigit():
			digits+=1
		elif c.isalpha():
			letters+=1
		else:
			print('ERROR')

	print("LETTERS " + str(letters))
	print("DIGITS " + str(digits))