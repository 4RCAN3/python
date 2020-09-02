#Represent a vector in multidimensional space
class Vector:

	#create d-dimensional vector of zeroes
	def __init__(self,d):
		self._coords=[0]*d

	#Return the dimension of the vector
	def __len__(self):
		return len(self._coords)

	#Return j-th coordinate of a vector
	def __getitem__(self,j):
		return self._coords[j]

	#Set j-th coordinate of a vector
	def __setitem__(self,j,val):
		self._coords[j]=val

	#Return sum of 2 vectors
	def __add__(self,other):
		if len(self)!=len(other):
			raise ValueError('dimensions must agree')
		result=Vector(len(self))
		for j in range (len(self)):
			result[j]=self[j]+other[j]
		return result

	#Returns true if a vector has same coordinates as other
	def __eq__(self,other):
		return self._coords==other._coords

	#Returns true if a vector differs from other
	def __ne__(self,other):
		return not self==other

	#Produce string representation of vector
	def __str__(self):
		return '<'+str(self._coords)[1:-1]+'>'

v=Vector(5)
for i in range(5):
	v[int(input())]
print(v)