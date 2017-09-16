import logging
import random
import string

logging.basicConfig(level=logging.WARNING)
logging.info("Attempting to import all from genetic.py...")
from genetic2 import *
logging.info("Successfully imported tools from genetic.")

POPULATION_SIZE = 500
global TARGET_STRING
TARGET_STRING = "to be or not to be"
global DNA_LENGTH
DNA_LENGTH = len(TARGET_STRING)
MUTATION_RATE = 1
TIME_DELAY = None


def randomString():
	# creates a random string of n letters
	charArray = string.ascii_lowercase + " "
	return ''.join([random.choice(charArray) for i in range(DNA_LENGTH)])

def mateStrings(mate1, mate2):
	#picks a random crossover point
	crossPoint = random.randint(0,len(mate1))
	return mate1[:crossPoint] + mate2[crossPoint:]

def mutateString(oldString, mutationRate):
	'''
	Mutates a string, given a percentage mutation rate
	'''
	#temporary variable
	mutationFlag = False

	newString = ""
	charArray = string.ascii_lowercase + " "
	for letter in oldString:
		if random.random()*100 < mutationRate:
			mutationFlag = True
			newString += random.choice(charArray)
		else:
			newString += letter

	if mutationFlag:
		logging.debug("MUTATION!  {} -> {}".format(oldString,newString))
	return newString


def fitnessFunction(s):
	assert len(s) == DNA_LENGTH
	correct = 0
	for i in range(len(s)):
		if s[i] == TARGET_STRING[i]:
			correct += 1
	return correct / DNA_LENGTH

def showStatus(self):
	'''
	This function will only work if it is passed into a population function as a method!
	'''
	#outputting the data
	pnt("\x1b[2J")
	pnt(pos(0,0))
	pnt("Current Best: {}\n".format(self.best))
	pnt("Fitness:      {}\n".format(self.bestFitValue))
	pnt("Generations:  {}\n".format(self.generations))
	# populationString = ", ".join([str(i) for i in self.popArray])
	# windowSize = shutil.get_terminal_size()
	# yCoor = 0
	# for i in textwrap.wrap(populationString, windowSize.columns - 70):
	# 	pnt70(yCoor,i)
	# 	yCoor += 1
	# 	if yCoor > windowSize.lines-1:
	# 		break

#some useful printing functions
def pos(x,y):
    return "\x1b[" + str(y) + ";" + str(x) + 'H'

def pnt(x):
	print(x,end='')

def pnt70(y,s):
	print(pos(70,y)+str(s))


testPopulation = Population(POPULATION_SIZE, randomString, mateStrings, mutateString, fitnessFunction, mutationRate=MUTATION_RATE, time_delay=TIME_DELAY, displayFunction=showStatus)
testPopulation.populate()
a = testPopulation.solve()
