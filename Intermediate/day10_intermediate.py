class Student:
	def __init__(self,age,weight,height):
		assert type(age) == int and age > 0, "Age can only be a positive integer"
		assert type(weight) == float and weight > 0 and weight == round(weight,2), "Weight should be a positive float"
		assert type(height) == float and height > 0 and height == round(height, 2), "The height should be a positive float"
		self.age = age
		self.weight = weight
		self.height = height
		
	def info(self):
		"""
		This function calculates the BMI of the Student according to the weight and height provided and returns a tuple of age and the calculated BMI
		"""
		bmi = self.weight/ (self.height ** 2)
		
		return self.age, round(bmi, 2)
		
		
def average(class_list):
	"""
	This function takes in a list of classes and returns the average of the ages, weights and heights of the different Student classes in the next 10 years.
	"""
	assert type(class_list) == list, "Only list of classes are expected"
	a = []
	w = []
	h = []
		
	for i in class_list:
		a.append(i.age + 10)
		w.append(i.weight*(1.05**10))
		h.append(i.height* (1.02**10))
	av_age = round(sum(a)/len(a), 2)
	av_weight = round(sum(w)/len(w), 2)
	av_height = round(sum(h)/len(h), 2)
	
	return av_age, av_weight, av_height
