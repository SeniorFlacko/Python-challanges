"""
Write a password generator in Python. Be creative with how you generate 
passwords - strong passwords have a mix of lowercase letters, uppercase letters, 
numbers, and symbols. The passwords should be random, generating a new password 
every time the user asks for a new password. 
Include your run-time code in a main method.


Extra:

Ask the user how strong they want their password to be. For weak passwords, 
pick a word or two from a list.


"""
import random
if __name__ == '__main__':
	print("Choose an option: ")
	print("1.- Weak")
	print("2.- Strong")
	lista_w = ["manzana","pera","mango","platano","naranja","limon","kiwi","papaya","rojo","verde","azul","blaco"]
	lista_s = ["!","#","$","_",".",0,1,2,3,4,5,6,7,8,9,"a","b","c","d","@","x","y",".","Z","O","K","D","R","X","W"]
	password=""
	o = int(input("Wich option: "))
	if o==1:
		for i in random.sample(lista_w,2):
			password+=i
	elif o==2:
		for i in random.sample(lista_s,8):
			password+=str(i)
	else:
		print(o)

	print(password)