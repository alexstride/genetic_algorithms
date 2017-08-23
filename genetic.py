import random
import string
global DNA_LENGTH
DNA_LENGTH = 10
import logging
logging.basicConfig(level=logging.DEBUG)
import numpy

class Session(object):
	pass

class Population(object):
	'''
	Methods:
	init: will create a new population, with a certain number of inds (n). Either from new or from an existing population.
	getFitness: will create a fitness array which will hold raw fitness information. Will store information about the best performer
	cumNormalize: will normalize fitnesses and add them cumulatively. Result should equal exactly 1.
	'''
	def __init__(self, n, creationFunction, fitnessFunction, matingFunction, mutationRate):
		self.n = n
		self.creationFunction = creationFunction
		self.fitnessFunction = fitnessFunction
		self.matingFunction = matingFunction
		logging.info("Creating a new population...")
		self.fitnesses = None
		self.cumNorm = None
		self.popArray = [Individual(True, function) for i in range(n)]
		logging.info("Population successfully created!")
		self.generations = 0

	def getFitnesses(f):
		self.fitnesses = map(f, popArray)
		total = sum(self.fitnesses)
		self.cumNorm = numpy.cumsum([i/total for i in self.fitnesses])

	def findBest():
		maxFit = self.fitnesses[0]
		curr = self.popArray[0]
		for i in range(self.n-1):
			if self.fitnesses[i] > maxFit:
				maxFit = self.fitnesses[i]
				curr = self.popArray[i]
		return (curr, maxFit)

	def findParent():
		assert cumNorm
		randomNum = random.random()
		for i in range(self.n - 1):
			if self.cumNorm[i] > randomNum:
				curr = self.popArray[i]
			else: 
				return curr


	def oneGeneration(printIntermediate=True):
		'''
		Should progress the population along by one generation
		'''
		logging.debug("calculating fitnesses...")
		self.getFitnesses(self.fitnessFunction)
		parent1 = self.findParent()
		parent2 = self.findParent()
		new = [Individual(False, self.matingFunction, parent1, parent2) for i in range(self.n)]
		for i in new:
			i.mutate(mutationRate)




class Individual(object):
	def __init__(self, new, *args):
		'''
		Initialises the Individual object
		If new is True then the function will try to create a new member using the next argument: (newFunction)
		If new is False, then next args must be (mateFunction, mate1, mate2)
		'''
		if new:
			self.DNA = args[0]()
		else:
			self.DNA = args[0](*args[1:])

	def __str__(self):
		return(self.DNA)

	def mutate(mutFunction, percentage):
		'''
		mutates the infomation in the individual based on the given function and percentage mutation rate
		'''
		pass




def randomString():
	# creates a random string of n letters
	charArray = string.ascii_lowercase + " "
	return ''.join([random.choice(charArray) for i in range(DNA_LENGTH)])

def mateStrings(mate1, mate2):
	#picks a random crossover point
	crossPoint = random.randint(0,len(mate1))
	return mate1[:crossPoint] + mate2[crossPoint:]






'''
#testing the randomString function.
# Should print 5x 3 letter random and 5x 10 letter random

for i in range(5):
	print(randomString(3))

for i in range(5):
	print(randomString(10))
'''

