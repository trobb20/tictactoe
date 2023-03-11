#!/usr/bin/python

####################IMPORTING STUFF#######################

import subprocess
from time import sleep
from imageHandler import *
from bot import *

###############READING FILES IF NEEDED########################

'''def readText(filename):
	with open(filename,'r') as text:
		info = text.read()
		return info

def writeText(filename,write):
	with open(filename, "w") as text:
		text.write(write)'''
		
##########################SETUP################################

try:
	from TTT_Images import * #try to import pillow 
except ImportError:
	openImg("title.jpg",[1,1,900,900])#if there is an error, user is starting script for first time. 
	changePosition("Terminal", [900,1]) #display launch screen and stuff
	
	print"-----------------------------------------------------"
	print"INPUT COMPUTER PASSWORD BELOW... INSTALLING PIP"
	print"-----------------------------------------------------"
	installPip=subprocess.Popen(['sudo','easy_install','pip']).wait() #install pip
	print"-----------------------------------------------------"
	print"INPUT COMPUTER PASSWORD BELOW... INSTALLING PILLOW"
	print"-----------------------------------------------------"
	subprocess.Popen(['xattr', '-d', 'com.apple.quarantine', "installPillow.command"]).wait() #allows pillow to be opened
	installPillow=subprocess.Popen(['open','installPillow.command']).wait() #install pillow
	
	counter=0 #counts number of seconds since started installing pillow
	
	while True:
		if counter<15: #if it has been less than 10 seconds since starting to install pillow
			try: #try to import pillow
				from TTT_Images import *
				print"-----------------------------------------------------"
				print"PILLOW INSTALL COMPLETE... STARTING TIC TAC TOE"
				print"-----------------------------------------------------"
				sleep(1)
				subprocess.Popen(["osascript", "-e", 'tell app "Terminal" to close front window']) #close front terminal window
				break
			except ImportError: #still hasnt installed yet
				sleep(1) #sleep 1 second
				counter=counter+1 #add 1 to counter
				continue
		print"-----------------------------------------------------"
		print"PILLOW DID NOT INSTALL. EXITING..."
		print"-----------------------------------------------------"
		break
	closeImg() #close title image
	
##################################CHOOSE:################################
while True:
	print "########################"
	print "WELCOME TO TIC TAC TOE!"
	print "########################"
	oneOrTwoPlayer=input("1 or 2 player? [type 1 or 2]: ")
	print "########################"
	one=False
	two=False
	if oneOrTwoPlayer==1:
		one=True
		break
	elif oneOrTwoPlayer:
		two=True
		break
	else:
		print "Incorrect input"
		continue
##################################ONE#####################################	
def onePlayer():
	
	changePosition("Terminal", [600,1]) #move terminal window
	board = [1,2,3,4,5,6,7,8,9]

	boardImage = makeBoard() #make board image
	boardImageUpscale=upscale(boardImage) #upscale it
	boardImageUpscale.save("boardImage.jpg","JPEG") #save it

	#this is key (board position) attached to list element (pixel position on board)
	imageDict = {7:[7,7],8:[24,7],9:[41,7],4:[7,24],5:[24,24],6:[41,24],1:[7,41],2:[24,41],3:[41,41]} 

	imageCoord=[]
	
	WIN_COMBINATIONS = (
		(1, 2, 3),
		(4, 5, 6),
		(7, 8, 9),
		(1, 4, 7),
		(2, 5, 8),
		(3, 6, 9),
		(1, 5, 9),
		(3, 5, 7),
	)
	
	def draw():
		print(board[6], board[7], board[8])
		print(board[3], board[4], board[5])
		print(board[0], board[1], board[2])
		
	def choose_number():
		while True:
			try:
				a = int(input())
				if a in board:
					closeImg() #close image after choosing 
					return a
				else:
					print("\nInvalid move. Try again")
			except ValueError:
			   print("\nThat's not a number. Try again")
	
	def is_game_over():
		#print WIN_COMBINATIONS
		for i in WIN_COMBINATIONS:
			if board[i[0]-1]==board[i[1]-1]==board[i[2]-1]:
				openImg("boardImage.jpg",[1,1,600,600]) #display image after winning
				print("Player %s wins!"%i[0])
				print("Congratulations!\n")
				return True
		if 9 == sum((pos == 'X' or pos == 'O') for pos in board):
			openImg("boardImage.jpg",[1,1,600,600]) #display image after tie
			print("The game ends in a tie\n")
			return True
			
	for player in "XO"*9:
		draw()
		if is_game_over():
			break
		if player=="X":
			print("Player %s pick your move"%player)
			
			openImg("boardImage.jpg",[1,1,600,600]) #display current board
			
			chosenNumber=choose_number() #number that is chosen
			
			board[chosenNumber-1]=player #re assign board to player's letter 
			
			imageCoord=imageDict[chosenNumber] #get the pixel location of the player's choice
			
			boardImage = writeX(boardImage, imageCoord[0], imageCoord[1])
			
		elif player == "O":
			(possibleMoves, winCombos, winPossible, winPossibleCombo, cornerstrat) = scanBoard(board, WIN_COMBINATIONS)
			
			chosenNumber = chooseMove(possibleMoves, winCombos, winPossible, winPossibleCombo, cornerstrat)
			
			print "Computer chose: "+str(chosenNumber)
			
			board[chosenNumber-1]=player #re assign board to player's letter
			
			(possibleMoves, winCombos, winPossible, winPossibleCombo, cornerstrat) = scanBoard(board, WIN_COMBINATIONS)
			
			imageCoord=imageDict[chosenNumber] #get the pixel location of the player's choice
			
			boardImage = writeO(boardImage, imageCoord[0], imageCoord[1])
		
		boardImageUpscale=upscale(boardImage) #upscale image
		boardImageUpscale.save("boardImage.jpg","JPEG") #save it 
		
#####################RAYANS CODE+EDITS (TWO)##############################

def tic_tac_toe():
	
	changePosition("Terminal", [600,1]) #move terminal window
	board = [None] + list(range(1, 10))

	boardImage = makeBoard() #make board image
	boardImageUpscale=upscale(boardImage) #upscale it
	boardImageUpscale.save("boardImage.jpg","JPEG") #save it

	#this is key (board position) attached to list element (pixel position on board)
	imageDict = {7:[7,7],8:[24,7],9:[41,7],4:[7,24],5:[24,24],6:[41,24],1:[7,41],2:[24,41],3:[41,41]} 

	imageCoord=[]

	WIN_COMBINATIONS = [
		(1, 2, 3),
		(4, 5, 6),
		(7, 8, 9),
		(1, 4, 7),
		(2, 5, 8),
		(3, 6, 9),
		(1, 5, 9),
		(3, 5, 7),
	]
	
	def draw():
		print(board[7], board[8], board[9])
		print(board[4], board[5], board[6])
		print(board[1], board[2], board[3])
		
	def choose_number():
		while True:
			try:
				a = int(input())
				if a in board:
					closeImg() #close image after choosing 
					return a
				else:
					print("\nInvalid move. Try again")
			except ValueError:
			   print("\nThat's not a number. Try again")
	
	def is_game_over():
		for a, b, c in WIN_COMBINATIONS:
			if board[a] == board[b] == board[c]:
				openImg("boardImage.jpg",[1,1,600,600]) #display image after winning
				print("Player {0} wins!\n".format(board[a]))
				print("Congratulations!\n")
				return True
		if 9 == sum((pos == 'X' or pos == 'O') for pos in board):
			openImg("boardImage.jpg",[1,1,600,600]) #display image after tie
			print("The game ends in a tie\n")
			return True
			
	for player in 'XO' * 9:
		draw()
		if is_game_over():
			break
		print("Player %s pick your move"%player)
		
		openImg("boardImage.jpg",[1,1,600,600]) #display current board
		
		chosenNumber=choose_number() #number that is chosen
		
		board[chosenNumber]=player #re assign board to player's letter 
		
		imageCoord=imageDict[chosenNumber] #get the pixel location of the player's choice
		
		if player=='X': #if player is x then write an x
			boardImage = writeX(boardImage, imageCoord[0], imageCoord[1])
		else: #if they are o then write an o
			boardImage = writeO(boardImage, imageCoord[0], imageCoord[1])
			 
		boardImageUpscale=upscale(boardImage) #upscale image
		boardImageUpscale.save("boardImage.jpg","JPEG") #save it 
		
########################
if one:
	while True:
		onePlayer()
		if raw_input("Play again (y/n)\n") != "y":
			closeImg()
			break

if two:		
	while True:
		tic_tac_toe()
		if raw_input("Play again (y/n)\n") != "y":
			closeImg()
			break
