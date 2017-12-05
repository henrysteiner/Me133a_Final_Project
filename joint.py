from sympy.vector import CoordSys3D

class Joint(object):

	def __init__(self, jType, ID):
		self.type = jType
		self.ID = ID
		self.coordSystem = CoordSys3D(str(ID))
		self.x = 0 # in relation to original
		self.y = 0 # in relation to original
		self.z = 0 # in relation to original




