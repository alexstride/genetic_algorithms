'''
File containing the Timetable object, as well as the lesson object, the pupil object and the teacher object
'''
import random, string


class Timetable(object):
	'''
	Class to hold the entire timetable array, there will be a two-dimensional array of lesson objects (format not decided). One dimension for time slot and one dimension for teacher.
	'''
	def __init__(self):
		pass

	def createArray(self, numPeriods, teacherArray, pupilArray):
		'''
		Creates an array of periods each containing a list of Lesson objects, which have been assigned to the appropriate teacher
		'''
		self.array = [[Lesson(j, i) for j in teacherArray] for i in range(numPeriods)]

class Lesson(object):
	'''
	Class to hold a particular instance of a lesson with a specific teacher.
	'''
	def __init__(self, teacher, period):
		self.teacher = teacher
		self.period = period
		self.pupils = []



class Teacher(object):
	'''
	Class to hold a teeacher, with attributes such as availability, skill level and allocation.
	'''
	def __init__(self, name, subject, allocation):
		self.name = name
		self.subject = subject
		self.allocation = allocation

	def getName(self):
		return self.name

	def getSubject(self): 
		return self.subject

	def getAllocation(self):
		return self.allocation

class Pupil(object):
	'''
	Class to hold information about a pupil, with information such as lesson-time requirements and ability information.
	Attributes:
	- code
	- yearGroup
	- requiredLessons
	- abilitySets
	'''
	def __init__(self, yearGroup):
		self.code = "".join([random.choice(string.ascii_lowercase) for i in range(10)])
		self.yearGroup = yearGroup
		self.requiredLessons = dict()
		self.abilitySets = dict()

	def getCode(self):
		return self.code

	def getYearGroup(self):
		return self.yearGroup

	def getRequiredLessons(self): 
		return self.requiredLessons

	def getAbilitySets(self):
		return self.abilitySets

class TeacherArray(object):
	'''To be written'''
	def __init__(self):
		self.isPopulated = False
		self.array = []

	def loadFromFile(self,filePath):
		def intLast(stringArray):
			#a function which is used to convert the final element(the allocation) into an int
			stringArray[-1] = int(stringArray[-1])
			return stringArray
		assert not self.isPopulated
		with open(filePath, 'r') as fileHandle:
			self.array = [Teacher(*intLast(i.split('\t'))) for i in fileHandle.read().split('\n') if not i=='']
		if len(self.array) > 0 : 
			self.isPopulated = True
		else:
			print("Array was not successfully populated.")


class PupilArray(object):
	'''To be written'''
		



