from sympy.vector import CoordSys3D
import math

class Joint(object):
	'''This class defines a Joint object as either prismatic or revolute, and contains its coordinate system
	location and orientation'''

	def __init__(self, jType, ID):
		self.type = jType # 0 for prismatic, 1 for revolute
		self.ID = ID
		self.coordSystem = CoordSys3D(str(ID))
		self.x = 0 # in relation to original
		self.y = 0 # in relation to original
		self.z = 0 # in relation to original

		self.d = 2
		self.theta = math.radians(90)
		self.r = 0
		self.alpha = math.radians(90)

	'''This function takes an initial joint object, a new joint object, and Denavit-Hartenberg parameters
	in order to calculate the new coordinate systems and location of the new joint (updating the new joint)'''
	def defineNew(self, prevJoint):

		# If the new joint is prismatic
		if self.type == 0:
			self.d = self.theta
			self.theta = 0

		# Retrieving the coordinate system from joint 1
		prevCoord = prevJoint.coordSystem

		# Rotating coordinate system by theta and alpha
		temp1 = prevCoord.orient_new_axis('temp1',self.theta, prevCoord.k)
		temp2 = temp1.orient_new_axis('temp2',self.alpha, prevCoord.i)

		# Translating coordinate system based on d (distance from previous joint to new joint along PREVIOUS z-axis)
		# and r (distance from previous joint to new joint along the NEW x-axis)
		newCoord = temp2.orient_new_axis('newCoord',0,temp2.k,location=(-self.d*prevCoord.k - self.r*temp2.i))

		# Redfining the new Joint's coordinate system
		self.coordSystem = newCoord

		# Computing the coordinates of the new coordinate frame with respect to the origin and defining the new Joint accordingly
		position = prevCoord.origin.express_coordinates(newCoord)	
		self.x = float(position[0])
		self.y = float(position[1])
		self.z = float(position[2])




