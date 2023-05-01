''' Hello guys in this code we have chosen a random number '18' and we gave 9 chances to pridict the number by the user '''


i=0
for i in range (1,10):
	print("You have remaining ", 10-i , "chances \n *Hint the nuber is from 1 to 20" )
	a=int(input("Enter you No. :- "))
	if a==18 :
		print("Cograts !", a, " is the corect number \n You won \n !!! Game Over !!!")
		break
	else :	
		print("Sorry !", a, " is the incorect number \n You loose ")
		
print ( "!!!  Game over !!!")	