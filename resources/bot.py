#!/usr/bin/python
'''
board = [1,2,3,4,5,6,7,8,9]

#####################TIC TAC TOE BOT####################
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
'''
positionAndBlock = {1:3,2:2,3:3,4:2,5:4,6:2,7:3,8:2,9:3} #list of positions as the key for the number of moves they block

def scanBoard(board, winCombos):
	
	possibleMoves = []
	cornerstrat=False
	
	winCombosList=[]
	for i in winCombos:
		winCombosList.append(list(i))
	
	#print winCombosList
	
	winPossible=False
	winPossibleCombo=[]
	
	for i in board:
		if not i == "X" and not i == "O":
			possibleMoves.append(i)
			
	#############CORNERSTRAT SCAN##############
	moveTally=0
	for i in board:
		try:	
			if i.isalpha():
				moveTally=moveTally+1
		except AttributeError:
			moveTally=0
	
	if moveTally<4:
		if board[4]=="O":
			if (board[0]=="X" and board[8]=="X") or (board[2]=="X" and board[6]=="X"):
				cornerstrat=True
			
	####MAKING WINCOMBOS####
	indexI=-1
	for i in board:
		indexI=indexI+1
		#print "Looking at: "+ str(i)
		if i=="O":
			#print "INDEX == "+str(indexI)
			previousNumber=indexI+1
			#print "Previous number: "+str(previousNumber)
			for j in winCombosList:
				for k in j:
					#print "Just looked at element: "+str(k)+" in list: "+str(j)
					if k == previousNumber:
						#print "MATCHED"
						j.insert(j.index(k), "O")
						j.remove(k)
						#print "J NOW == "+str(j)
		elif i=="X":
		#	print "INDEX == "+str(indexI)
			previousNumber=indexI+1
			#print "Previous number: "+str(previousNumber)
			for j in winCombosList:
				for k in j:
					#print "Just looked at element: "+str(k)+" in list: "+str(j)
					if k == previousNumber:
						#print "MATCHED"
						j.insert(j.index(k), "X")
						j.remove(k)
						#print "J NOW == "+str(j)
						
	for i in winCombosList:
		if 'O' in i and not "X" in i:
			tally = 0
			for j in i:
				if j=='O':
					tally=tally+1
			if tally>1:
				winPossible=True
				#print "WIN POSSIBLE"
				winPossibleCombo = i
	
		
	if winPossible==False:
		#print 'WIN NOT POSSIBLE THIS TIME'
		winPossibleCombo=[]
		winCombosNoO=winCombosList
		for i in winCombosNoO[:]:
			#print str(i) + " :JUST LOOPED THROUGH"
			if 'O' in i:
			#print str(i) + ": FOUND A O IN"
				winCombosNoO.remove(i)
		#print "PASSED THROUGH: "
		#print possibleMoves, winCombosNoO, winPossible, winPossibleCombo
		return possibleMoves, winCombosNoO, winPossible, winPossibleCombo, cornerstrat
	else:
		#print "PASSED THROUGH: "
		#print possibleMoves, winCombosList, winPossible, winPossibleCombo
		return possibleMoves, winCombosList, winPossible, winPossibleCombo, cornerstrat
	
	#print "SCANNED BOARD. BOARD == "+str(board)
			
	#print "WINCOMBOS NOW == "+str(winCombos)
				
	
	

	
def chooseMove(possibleMoves, winCombos, winPossible, winPossibleCombo, cornerstrat):
	
	#print "------------------------"
	#print "Choosing Move:"
	
	choice = 0
	
	doubleX=False
	singleX=False
	
	doubleXList=[]
	singleXList=[]
	
	########################OFFENSE############################	
	if winPossible:
		#print "WIN POSSIBLE"
		for i in winPossibleCombo:
			if not i == "O":
				choice = i
				return choice
				
	####################CORNERSTRAT#####################
	
	if cornerstrat:
		for i in possibleMoves:
			if i%2==0:
				choice=i
				return choice
	
	########################DEFENSE############################
			
	xInCombos=0 #counter for #of x in combos
	
	winCombosDict={} #win combo index as key for #of X's in that combo
			
	for i in winCombos:
		xInCombos=0 #set to 0
		for j in i:
			if j=="X":
				xInCombos=xInCombos+1 #if it finds an X add one
		if xInCombos==2: 
			winCombosDict[winCombos.index(i)]=2 #assign value 2 to key index of i
		elif xInCombos==1:
			winCombosDict[winCombos.index(i)]=1 #assign 1
		else:
			winCombosDict[winCombos.index(i)]=0 #assign 0
			
	#print "WinCombosDict now == "+str(winCombosDict)
			
	for i in range(0,len(winCombos)):
		if winCombosDict[i]==2: #if there are 2 X in any win combo, doubleX = true
			doubleX=True
			doubleXList.append(i) #add the index of the wincombo in winCombos to doubleXList
		elif winCombosDict[i]==1: #same as above but for if there is only 1 x in a wincombo
			singleX=True
			singleXList.append(i)

	if doubleX: #if there is an instance of doubleX
		#print "DOUBLEX"
		if len(doubleXList)>1: #if there are 2 combos with 2 x's we've lost
			print "You beat me...somehow"
		else:
			#print "SINGLE INSTANCE DOUBLEX"
			for i in winCombos[doubleXList[0]]: #otherwise, if there is only one combo with doubleX then block it.
				if not i=="X":
					choice = i
	elif singleX and not doubleX: #if there is an instance of singleX
		#print "SINGLEX"
		if len(singleXList)>1: #more than one instance
			#print "MORE THAN 1 INSTANCE SINGLEX"
			print singleXList
			choiceSet=[]
			choiceSetBlocks=[]
			for i in singleXList:
				for j in winCombos[i]:
					if type(j)==int:
						choiceSet.append(j)
						choiceSetBlocks.append(positionAndBlock[j])
			choice = max(set(choiceSet), key=choiceSet.count)
			count = 0 
			for i in choiceSet:
				if i == choice:
					count=count+1
			if not count>1:
				choice = choiceSet[choiceSetBlocks.index(max(choiceSetBlocks))]

		else: #one instance
			#print "ONLY 1 INSTANCE SINGLEX"
			choiceSet=[] 
			choiceSetBlocks=[]
			for i in winCombos[singleXList[0]]:
				if not i=="X":
					choiceSet.append(i)
					choiceSetBlocks.append(positionAndBlock[i])
			choice = choiceSet[choiceSetBlocks.index(max(choiceSetBlocks))]
	elif not singleX and not doubleX:
		#print "NO THREATS"
		choiceSet=[]
		choiceSetBlocks=[]
		for i in winCombos:
			for j in i:
				if type(j)==int:
					choiceSet.append(j)
					choiceSetBlocks.append(positionAndBlock[j])
		choice = choiceSet[choiceSetBlocks.index(max(choiceSetBlocks))]
					
	if not choice in possibleMoves:
		print "ERROR"
		
	return choice
'''	
winCombosNoO=WIN_COMBINATIONS
	
while len(winCombosNoO)>0:
	inp = input("Select square: ")
	for i in board:
		if i==inp:
			board.insert(board.index(i), "X")
			board.remove(i)
	(possibleMoves, winCombos, winPossible, winPossibleCombo, cornerstrat) = scanBoard(board, WIN_COMBINATIONS)
	choice = chooseMove(possibleMoves, winCombos, winPossible, winPossibleCombo, cornerstrat)
	print "Computer chose: "+str(choice)
	print "------------------------"
	for i in board:
		if i==choice:
			board.insert(board.index(i), "O")
			board.remove(i)
	(possibleMoves, winCombos, winPossible, winPossibleCombo, cornerstrat) = scanBoard(board, WIN_COMBINATIONS)'''
				