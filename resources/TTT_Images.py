#!/usr/bin/python

from PIL import Image
import subprocess
from imageHandler import *
from time import sleep

def makeBoard():
	ticTacToe = Image.new("RGB", (49,49), "White")

	pixelMap = ticTacToe.load()

	for i in range(0,49):
		pixelMap[15,i]=(0,0,0)
		pixelMap[16,i]=(0,0,0)
	
		pixelMap[32,i]=(0,0,0)
		pixelMap[33,i]=(0,0,0)
	
		pixelMap[i,15]=(0,0,0)
		pixelMap[i,16]=(0,0,0)
	
		pixelMap[i,32]=(0,0,0)
		pixelMap[i,33]=(0,0,0)
	
	return ticTacToe

def bigPixel(pixelMap,locationX,locationY):
	
		pixelMap[locationX-1,locationY-1]=(0,0,0)
		pixelMap[locationX,locationY-1]=(0,0,0)
		pixelMap[locationX+1,locationY-1]=(0,0,0)
	
		pixelMap[locationX-1,locationY]=(0,0,0)
		pixelMap[locationX,locationY]=(0,0,0)
		pixelMap[locationX+1,locationY]=(0,0,0)
	
		pixelMap[locationX-1,locationY+1]=(0,0,0)
		pixelMap[locationX,locationY+1]=(0,0,0)
		pixelMap[locationX+1,locationY+1]=(0,0,0)

def writeX(board, locationX, locationY):
	
	pixelMap = board.load()
	
	bigPixel(pixelMap, locationX-3, locationY-3) #top row
	bigPixel(pixelMap, locationX+3, locationY-3)

	bigPixel(pixelMap, locationX, locationY) #middle row
	
	bigPixel(pixelMap, locationX-3, locationY+3) #bottom row
	bigPixel(pixelMap, locationX+3, locationY+3)
	
	return board
	
def writeO(board, locationX, locationY):
	
	pixelMap = board.load()
	
	bigPixel(pixelMap, locationX-3, locationY-3) #top row
	bigPixel(pixelMap, locationX+3, locationY-3)
	bigPixel(pixelMap, locationX, locationY-3) #top row
	
	bigPixel(pixelMap, locationX-3, locationY) #middle row
	bigPixel(pixelMap, locationX+3, locationY)
	
	bigPixel(pixelMap, locationX, locationY+3) #bottom row
	bigPixel(pixelMap, locationX-3, locationY+3) #bottom row
	bigPixel(pixelMap, locationX+3, locationY+3)
	
	return board
	
def upscale(board):
	board=board.resize((600,600), Image.ANTIALIAS)
	return board
	
#openImg("boardImage.jpg", 5)

board=makeBoard()


