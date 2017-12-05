from matplotlib.widgets import Slider, RadioButtons, Button
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from joint import Joint

class Show_GUI():

	def __init__(self):

		# Initialize all the variables
		self.fig = plt.figure("DH Parameters	Robot Simulator")  #create the frame
		self.axes = plt.axes([0.05, 0.2, 0.90, 0.75], projection='3d')

		self.theta_val = 90
		self.d_val = 0
		self.r_val = 0
		self.alpha_val = 0

		self.joints = []
		self.numJoints = 3

		for i in range(self.numJoints):
			joint = Joint(1, i+1)
			self.joints.append(joint)

		self.currentJoint = self.joints[0]

		self.drawJoints()

		# Draw Theta slider panel
		thetaVals = plt.axes([0.35, 0.1425, 0.45, 0.03])
		theta_slide = Slider(thetaVals, 'Theta Value', 0.0, 360, valinit=90)
		
		# Draw D slider panel
		dVals = plt.axes([0.35, 0.1, 0.45, 0.03])
		d_slide = Slider(dVals, 'D Value', 0.0, 300, valinit=0)

		# Draw A slider panel
		rVals = plt.axes([0.35, 0.0575, 0.45, 0.03])
		r_slide = Slider(rVals, 'R Value', 0.0, 300, valinit=0)

		# Draw Alpha slider panel
		alphaVals = plt.axes([0.35, 0.015, 0.45, 0.03])
		alpha_slide = Slider(alphaVals, 'Alpha Value', -180, 180, valinit=0)

		# Create radio button
		jointType = plt.axes([0.05, 0.02, 0.15, 0.12])
		jointType.set_title('Joint Type', fontsize=12)
		jointOptions = RadioButtons(jointType, ('Prismatic', 'Revolute'), active=1)

		# Create radio button
		jointNum = plt.axes([0.05, 0.20, 0.15, 0.12])
		jointNum.set_title('Which Joint', fontsize=12)
		jointNum = RadioButtons(jointNum, (1, 2, 3, 4), active=1)

		def update_link():
			if self.currentJoint.ID != self.numJoints:
				newJoint = self.joints[self.currentJoint.ID]
				self.currentJoint.defineNew(self.d_val, self.theta_val, self.r_val, self.alpha_val, newJoint)
				self.drawJoints()

		def getTheta(val):
			self.theta_val = val
			update_link()

		def getD(val):
			self.d_val = val
			update_link()

		def getR(val):
			self.r_val = val
			update_link()

		def getAlpha(val):
			self.alpha_val = val
			update_link()

		theta_slide.on_changed(getTheta)
		d_slide.on_changed(getD)
		r_slide.on_changed(getR)
		alpha_slide.on_changed(getAlpha)

		def changeCurrentJoint(label):
			self.currentJoint = self.joints[label-1]

		jointNum.on_clicked(changeCurrentJoint)

		plt.show()

	def fillArrays(self):
		x = []
		y = []
		z = []
		for i in range(self.numJoints):
			x.append(self.joints[i-1].x)
			y.append(self.joints[i-1].y)
			z.append(self.joints[i-1].z)

		self.x = np.array(x)
		self.y = np.array(y)
		self.z = np.array(z)

	def plotCoordinateSystem(self):
		for i in range(self.numJoints):
			joint = self.joints[i]

			posX = joint.x
			posY = joint.y
			posZ = joint.z
			lineDist = 0.5

			if joint.ID == 1:
			   xs = list((posX, posX + lineDist))
			   ys = list((posY, posY))
			   zs = list((posZ, posZ))
			   self.axes.plot(xs, ys, zs, linewidth = 1, color="green")
			   xs = list((posX, posX))
			   ys = list((posY, posY + lineDist))
			   zs = list((posZ, posZ))
			   self.axes.plot(xs, ys, zs, linewidth = 1, color="blue")
			   xs =list((posX, posX))
			   ys = list((posY, posY))
			   zs = list((posZ, posZ + lineDist))
			   self.axes.plot(xs, ys, zs, linewidth = 1, color="red")
			elif joint.type == 1:
			   xs = list((posX, posX + lineDist))
			   ys = list((posY, posY))
			   zs = list((posZ, posZ))
			   self.axes.plot(xs, ys, zs, linewidth = 1, color="green")
			   xs = list((posX, posX))
			   ys = list((posZ, posZ - lineDist))
			   zs = list((posY, posY))
			   self.axes.plot(xs, zs, ys, linewidth = 1, color="blue")
			   xs =list((posX, posX))
			   ys = list((posZ, posZ))
			   zs = list((posY, posY + lineDist))
			   self.axes.plot(xs, zs, ys, linewidth = 1, color="red")
			elif joint.type == 0:
			   xs = list((posY, posY + lineDist))
			   ys = list((posX, posX))
			   zs = list((posZ, posZ))
			   self.axes.plot(ys, xs, zs, linewidth = 1, color="green")
			   xs = list((posX, posX))
			   ys = list((posZ, posZ + lineDist))
			   zs = list((posY, posY))
			   self.axes.plot(xs, zs, ys, linewidth = 1, color="blue")
			   zs = list((posX, posX + lineDist))
			   xs =list((posZ, posZ))
			   ys = list((posY, posY))
			   self.axes.plot(zs, ys, xs, linewidth = 1, color="red")

	def plotJoints(self):
		self.fillArrays()
		x = np.array(self.x).tolist()
		y = np.array(self.y).tolist()
		z = np.array(self.z).tolist()

		self.axes.cla() # clear current axis

		# draw lines and faces
		self.axes.plot(x, y, z, 'o-', markersize=20,
			markerfacecolor="orange", linewidth=8, color="blue")
		self.axes.plot(x, y, z, 'o-', markersize=4,
			markerfacecolor="blue", linewidth=1, color="silver")

	def set_axes(self):

		self.axes.set_xlim3d(-200, 200)
		self.axes.set_ylim3d(-200, 200)
		self.axes.set_zlim3d(-5, 200)
		self.axes.set_xlabel('X axis')
		self.axes.set_ylabel('Y axis')
		self.axes.set_zlabel('Z axis')

		for j in self.axes.get_xticklabels() + self.axes.get_yticklabels() + self.axes.get_zticklabels(): #hide ticks
			j.set_visible(False)

	def drawJoints(self):
		self.set_axes()
		self.plotJoints()
		self.plotCoordinateSystem()

		plt.draw()

if __name__ == '__main__':
	gui = Show_GUI()




