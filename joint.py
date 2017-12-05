class Joint(object):

	def __init__(self, jType, ID):
		self.type = jType
		self.ID = ID
		self.coordSystem = CoordSys3D(str(ID))


