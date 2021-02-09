from datetime import datetime

class Person:

	def __init__(self, name, surname):

		self.name = name
		self.surname = surname
		self.registration_date = datetime.now() # data di registrazione

	def since(self):

		return(datetime.now() - self.registration_date).seconds

p1 = Person('Tim', 'Peters')
p2 = Person('Raymond', 'Hettinger')
p2.since()
