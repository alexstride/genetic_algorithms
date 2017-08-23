import string
import random
from timetable import *
import pytest

newTeacherArray = TeacherArray()
newTeacherArray.loadFromFile('teachers')

@pytest.mark.parametrize("teacherObject",newTeacherArray.array)
def test_isValidTeacher(teacherObject):
	name = teacherObject.getName()
	subject = teacherObject.getSubject()
	allocation = teacherObject.getAllocation()
	assert type(name) == str
	assert len(name) > 0
	assert type(subject) == str
	assert len(subject) > 0
	assert type(allocation) == int


