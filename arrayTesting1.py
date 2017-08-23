import numpy as np

teachers = ["A", "B"]
pupils = ["P{}".format(i+1) for i in range(20)]
timeslots = [1,2,3,4]

print(teachers)
print(pupils)
print(timeslots)

array = np.zeros((len(teachers),len(timeslots),len(pupils)), dtype=bool)

print(array)

