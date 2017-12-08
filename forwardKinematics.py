import numpy as np
import math
import csv
import time 

# This function creates the forward kinematics parameters using the joints
def generateFK(joints, filename):

	fKMap = generateTransformation(joints[1])
	params = []
	params.append([1, joints[1].theta, joints[1].d, joints[1].r, joints[1].alpha])

	for i in range(2, len(joints)):
		temp = generateTransformation(joints[i])
		fKMap = fKMap.dot(temp)

		params.append([i, joints[i].theta, joints[i].d, joints[i].r, joints[i].alpha])

	# Keeps appending to the file so as not to lose data.
	with open(filename, 'a') as f:
		writer = csv.writer(f)
		writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S')])
		writer.writerow(['Forward Kinematics Map'])
		np.savetxt(f, fKMap, delimiter=',')
		writer.writerow([''])
		writer.writerow(['Link', 'Theta', 'D', 'R', 'Alpha'])
		np.savetxt(f, params, delimiter=',')
		writer.writerow([''])

	f.close()

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
