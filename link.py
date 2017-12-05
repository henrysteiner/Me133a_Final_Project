def createLink(d,theta,r,alpha,prevJoint,newJoint):
	'''This function takes an initial joint object, a new joint object, and Denavit-Hartenberg parameters
	in order to calculate the new coordinate system and location of the new joint'''

		if newJoint.jtype == 0: #  0 for prismatic, 1 for revolute
			d = theta
			theta = 0

		# Retrieving the coordinate system from joint 1
		prevCoord = prevJoint.coordSystem

		# Rotating coordinate system by theta and alpha
		temp1 = prevCoord.orient_new_axis('temp1',theta, prevCoord.k)
		temp2 = temp1.orient_new_axis('temp2',alpha, prevCoord.i)

		# Translating coordinate system based on d (distance from previous joint to new joint along PREVIOUS z-axis)
		# and r (distance from previous joint to new joint along the NEW x-axis)
		newCoord = temp2.orient_new_axis('newCoord',0,temp2.k,location=d*prevCoord.k + r*temp2.i)

		# Redfining the new Joint's coordinate system
		newJoint.coordSystem = newCoord

		# Creating an origin reference
		origin = CoordSys3D('origin')

		# Computing the coordinates of the new coordinate frame with respect to the origin and defining the new Joint accordingly
		position = origin.origin.express_coordinates(newCoord)
		newJoint.x = position[0]
		newJoint.y = position[1]
		newJoint.z = position[2]







