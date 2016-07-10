#!/usr/bin/python
from random import uniform
from math import ceil
import logging

def swap_list_items(i,j,listOfChars):
	listOfChars[i], listOfChars[j] = listOfChars[j], listOfChars[i]

def shuffle(refString="aabbccddeeffgghhiijj"):
	listOfChars = [c for c in refString]
	index = 0
	for c in listOfChars:
		swap_list_items(index, int(ceil(uniform(0,19))), listOfChars)
		index += 1
	return listOfChars

def game_loop(counter, fillString):
	boxes = {}
	shuffledList = shuffle(fillString)
	for i in range(0, len(fillString)):
		boxes[i] = shuffledList[i] 
		logging.warning( i, "=>", boxes[i]
	lucky_boxes = []
	while((counter > 0) and (len(boxes) > 0) ):
		selected_box = int(input("Please, select a box number [1-20]: ")) - 1
		lucky_character = boxes[selected_box]
		lucky_boxes.append((lucky_character, selected_box))
		if (len(lucky_boxes) > 1) and (lucky_boxes[-1][0] == lucky_boxes[-2][0]):
			print lucky_boxes[-1][1]
			print lucky_boxes[-2][1]
			boxes.pop(lucky_boxes[-1][1])
			boxes.pop(lucky_boxes[-2][1])
		counter -= 1
	else:
		if len(boxes) > 0:
			print("Hard luck, you lost")
		else:
			print("congratulations you won!")


counter = 40
fillString = "aabbccddeeffgghhiijj"
game_loop(counter, fillString)