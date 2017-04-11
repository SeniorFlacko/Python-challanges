"""
Make a two-player Rock-Paper-Scissors game. 

Hint:
Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game


"""
lista = [("Paper","Rock"),("Rock","Scissors"),("Scissors","Paper")]
def who_win(player1,player2):
	if (player1,player2) in lista:
		return 'player1 wins'
	elif (player2,player1) in lista:
		return 'player2 wins'
	else:
		return 'Draw'

if __name__ == '__main__':

	a=''
	b=''
	ans = 'y'
	while ans!='n':
		a = input('What do you play Rock or Paper or Scissors? ')
		b = input('What do you play Rock or Paper or Scissors? ')
		print(who_win(a,b))
		ans = input("Do you want to continue: y/n ")
