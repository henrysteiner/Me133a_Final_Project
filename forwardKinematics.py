import numpy as np
import math

# This function creates the forward kinematics parameters using the joints
def generateFK(joints):

	fKMap = generateTransformation(joints[1])
	params = [['Link', 'Theta', 'D', 'R', 'Alpha']]
	params.append([1, joints[1].theta, joints[1].d, joints[1].r, joints[1].alpha])

	for i in range(2, len(joints)):
		temp = generateTransformation(joints[i])
		fKMap = fKMap.dot(temp)

		params.append([i, joints[i].theta, joints[i].d, joints[i].r, joints[i].alpha])

	for row in fKMap:
		print row

	for row in params:
		print row

def generateTransformation(j):

	mat = []

	row1 = [math.cos(j.theta), -math.sin(j.theta)*math.cos(j.alpha), 
		math.sin(j.theta)*math.sin(j.alpha), j.r*math.cos(j.theta)]

	row2 = [math.sin(j.theta), math.cos(j.theta)*math.cos(j.alpha),
		-math.cos(j.theta)*math.sin(j.alpha), j.r*math.sin(j.theta)]

	row3 = [0, math.sin(j.alpha), math.cos(j.alpha), j.d]

	row4 = [0, 0, 0, 1]

	mat = [row1, row2, row3, row4]
	return np.matrix(mat)
