#!/usr/bin/python

#Teddy's Image Handler.

import subprocess
from time import sleep

def changePosition(app,location): #this takes an app and a location and moves the window to that location
	subprocess.Popen(['osascript','-e','tell app "%s" to set position of front window to {%d,%d}'%	(app,location[0],location[1])])

def changeBounds(app,location): #this takes an app and location and resizes the app's front window to that location and size
	subprocess.Popen(['osascript','-e','tell app "%s" to set bounds of front window to {%d,%d,%d,%d}'%	(app,location[0],location[1],location[2],location[3])])

def openImg(imgPath,location): #this opens an image in preview, then changes its boundaries to whatever you want
	viewerOpen = subprocess.Popen(['open','-a','Preview',imgPath])
	sleep(0.05)
	changeBounds("Preview", location)
	return viewerOpen

def closeImg(): #this closes preview's current image
	subprocess.Popen(["osascript", "-e", 'tell app "Preview" to close front window'])

#openImg("title.jpg",[1,1,900,900])
