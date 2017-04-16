"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

"""
if __name__ == '__main__':
	cadena = input("Ingrese dos numeros separados por coma: ")
	lista = cadena.split(',')
	x = int(lista[0])
	y = int(lista[1])
	matriz = []
	for i in range(x):
		matriz.append([0]*y)

	for i in range(x):
		for j in range(y):
			matriz[i][j]=i*j
	
	print(matriz)