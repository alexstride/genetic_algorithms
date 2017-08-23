#importing necessary packages
import logging
import numpy as np
import random
import time
import shutil
import textwrap
import pdb

class Session(object):
	pass

class Population(object):
	'''
	An object to hold all of the individuals and computations needed to carry out evolution

	Methods:
	- __init__
	- __str__
	- solve
	- oneGeneration
	- populateFitnesses
	- setBest
	- populate
	- updatePopulation
	- printPopulation
	- printFitnessStats
	- yieldParents	
	'''
	def __init__(self, size,  creationFunction, matingFunction, mutationFunction, fitnessFunction, mutationRate=2, time_delay=None, displayFunction=None):
		logging.debug("Initializing population of size {}...".format(size))
		self.n = size
		self.createInd = creationFunction
		self.mateInds = matingFunction
		self.mutateInd = mutationFunction
		self.fitnessInd = fitnessFunction
		self.mutationRate = mutationRate
		self.popArray = None
		self.generations = 0
		self.fitnesses = np.zeros((self.n,2))
		self.best = None
		self.bestFitValue = 0
		self.time_delay = time_delay
		logging.info("Population successfully created!")
		self.showStatus = displayFunction

	def __str__(self):
		if self.popArray:
			return str(self.popArray)
		else:
			return "Population object. Not yet populated"

	def solve(self):
		while True:
			if self.time_delay:
				time.sleep(self.time_delay)
			#uncomment to debug
			#input("Press enter...")
			self.oneGeneration()
			if self.fitnessInd(self.best.getDNA()) > 0.9999:
				return self.best

	def oneGeneration(self):
		logging.info("Creating generation {}...".format(self.generations + 1))
		#Checks whether the popArray has actually been populated
		if not self.popArray:
			logging.warning("Cannot proceed as population is empty!")
		else:
			#assessing the fitnesses of all of the elements in popArray
			self.populateFitnesses()
			self.setBest()
			self.updatePopulation()
			self.generations += 1
			if self.showStatus: self.showStatus(self)

	def populateFitnesses(self):
		'''
		First creates array of fitnesses, then normalizes so that the array sums to 1
		'''
		self.fitnesses = np.array([self.fitnessInd(i.getDNA()) for i in self.popArray])


	def setBest(self):
		'''
		Finds the fittest current memeber of the population, sets it to self.best and prints out some information.
		'''
		currBest = np.max(self.fitnesses)
		if currBest > self.bestFitValue:
			self.bestFitValue = currBest
			self.best = self.popArray[np.argmax(self.fitnesses)]
		logging.info("Best fit is: {} \t\t\tFitness: {}".format(self.best, self.bestFitValue))

	def populate(self):
		'''
		Set the initial population of popArray
		'''
		self.popArray = [Individual() for i in range(self.n)]
		for i in self.popArray: i.addDNA(self.createInd())

	def updatePopulation(self):
		'''
		Updates the population by creating a new popArray based on the fitness values already calculated.
		'''
		newPop = []
		
		#loop over the size of the desired new population (will always be self.n)
		for parents in self.yieldParents():
			newIndividual = Individual()
			newDNA = self.mateInds(parents[0].getDNA(),parents[1].getDNA())
			newDNA = self.mutateInd(newDNA, self.mutationRate)
			newIndividual.addDNA(newDNA)
			newPop.append(newIndividual)
			#DEBUGGING CODE: Some code to print out each set of parents.
			#print("Parent1: {}({})   Parent2: {}({})   Child: {}({})".format(parents[0], self.fitnessInd(parents[0].getDNA()), parents[1], self.fitnessInd(parents[1].getDNA()), newIndividual.getDNA(), self.fitnessInd(newIndividual.getDNA()) ))

		assert len(newPop) == self.n
		self.popArray = newPop

	def printPopulation(self):
		curr = 0
		for i in self.popArray:
			print("{}\t".format(i),end="")
			curr += 1
			if curr%10 == 0:
				print("")

	def printFitnessStats(self):
		mean = np.mean(self.fitnesses)
		print("The mean of the fitnesses is: {}".format(mean))
		print("The median of the fitnesses is {}".format(np.median(self.fitnesses)))

	def yieldParents(self):
		'''
		Creates a mating pool which is 10 times the size of the population

		The normalizing of the fitness function has now been moved to here
		'''
		#normalizing fitnesses
		total = sum(self.fitnesses)
		#goes through and divides by total; could be more memory efficient.
		normalized = np.array([i/total for i in self.fitnesses])
		logging.debug(normalized)

		MATING_POOL_SIZE = self.n * 5
		matingPool = []
		for i in range(self.n):
			num = int(normalized[i] * (self.n * 5))
			for k in range(num): 
				matingPool.append(self.popArray[i])

		for j in range(self.n):
			yield (random.choice(matingPool), random.choice(matingPool))









class Individual(object):
	'''
	Notably more passive than the older incarnation of individual.

	Methods:
	- addDNA(DNA) - Adds some DNA to the object
	- getDNA() - Returns the current DNA of the object

	'''
	def __init__(self):
		self.DNA = None

	def __str__(self):
		return self.DNA

	def addDNA(self, newDNA):
		self.DNA = newDNA

	def getDNA(self):
		return self.DNA



#Application specific functions
