"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.

Hint
Use __init__ method to construct some parameters


"""
class strup:
	def __init__(self,cadena):
		self.cadena=cadena

	def getString(self):
		s = input()
		self.cadena=s
		return s

	def printString(self):
		return self.cadena.upper()

if __name__== '__main__':
	obj = strup("")
	obj.getString()
	print(obj.printString())
