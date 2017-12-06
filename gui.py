from matplotlib.widgets import Slider, RadioButtons, Button
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from joint import Joint
import math

class Show_GUI():

	def __init__(self):

		# Initialize all the variables
		self.fig = plt.figure("DH Parameters	Robot Simulator")  #create the frame
		self.axes = plt.axes([0.05, 0.2, 0.90, 0.75], projection='3d')
		self.axes.set_autoscale_on(False)

		self.joints = []
		self.numJoints = 4

		for i in range(self.numJoints):
			joint = Joint(1,i)
			self.joints.append(joint)

		self.currentJoint = self.joints[1]
		self.drawJoints()

		# Draw Theta slider panel
		thetaVals = plt.axes([0.35, 0.1425, 0.30, 0.03])
		self.theta_slide = Slider(thetaVals, 'Theta Value', 0.0, 360, valinit=math.degrees(self.currentJoint.theta))
		
		# Draw d slider panel
		dVals = plt.axes([0.35, 0.1, 0.30, 0.03])
		self.d_slide = Slider(dVals, 'D Value', 0.0, 10, valinit=self.currentJoint.d)

		# Draw r slider panel
		rVals = plt.axes([0.35, 0.0575, 0.30, 0.03])
		self.r_slide = Slider(rVals, 'R Value', 0.0, 10, valinit=self.currentJoint.r)

		# Draw Alpha slider panel
		alphaVals = plt.axes([0.35, 0.015, 0.30, 0.03])
		self.alpha_slide = Slider(alphaVals, 'Alpha Value', -180, 180, valinit=math.degrees(self.currentJoint.alpha))

		# Create radio button
		linkNum = plt.axes([0.05, 0.02, 0.15, 0.12])
		linkNum.set_title('Link Number', fontsize=12)
		linkNum_Radio = RadioButtons(linkNum, list(range(1,self.numJoints)), active=0)

		# Create radio button
		jointType = plt.axes([0.75, 0.02, 0.15, 0.12])
		jointType.set_title('Joint Type', fontsize=12)
		types = {'Prismatic': 0, 'Revolute': 1}
		self.jointOptions = RadioButtons(jointType, types.keys(), active=1)

		def update_link():
			curID = self.currentJoint.ID
			while curID < self.numJoints:
				oldJoint = self.joints[curID - 1]
				curJoint = self.joints[curID]

				curJoint.defineNew(oldJoint)
				curID += 1

			self.drawJoints()

		def getTheta(val):
			self.currentJoint.theta = math.radians(val)
			update_link()

		def getD(val):
			self.currentJoint.d = val
			update_link()

		def getR(val):
			self.currentJoint.r = val
			update_link()

		def getAlpha(val):
			self.currentJoint.alpha = math.radians(val)
			update_link()

		def changeType(val):
			self.currentJoint.type = types[val]
			update_link()

		def changeCurrentLink(label):
			self.currentJoint = self.joints[int(label)]
			self.theta_slide.set_val(math.degrees(self.currentJoint.theta))
			self.d_slide.set_val(self.currentJoint.d)
			self.r_slide.set_val(self.currentJoint.r)
			self.alpha_slide.set_val(math.degrees(self.currentJoint.alpha))
			#self.jointOptions.set_active(self.currentJoint.type)
			self.jointOptions.active = self.currentJoint.type

		self.theta_slide.on_changed(getTheta)
		self.d_slide.on_changed(getD)
		self.r_slide.on_changed(getR)
		self.alpha_slide.on_changed(getAlpha)

		linkNum_Radio.on_clicked(changeCurrentLink)
		self.jointOptions.on_clicked(changeType)

		plt.show()

	def fillArrays(self):
		x = []
		y = []
		z = []
		for i in range(self.numJoints):
			x.append(self.joints[i].x)
			y.append(self.joints[i].y)
			z.append(self.joints[i].z)

		self.x = np.array(x)
		self.y = np.array(y)
		self.z = np.array(z)

	def plotCoordinateSystem(self):
		for i in range(self.numJoints):
			joint = self.joints[i]

			posX = joint.x
			posY = joint.y
			posZ = joint.z
			lineDist = 5

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
		for i in range(0,len(x)):
			self.axes.text(x[i],y[i],z[i],"Joint " + str(i),color='black')

	def set_axes(self):

		self.axes.set_xlim3d(-10, 10)
		self.axes.set_ylim3d(-10, 10)
		self.axes.set_zlim3d(-10, 10)
		self.axes.set_xlabel('X axis')
		self.axes.set_ylabel('Y axis')
		self.axes.set_zlabel('Z axis')

	def drawJoints(self):
		self.plotJoints()
		self.plotCoordinateSystem()
		
		plt.draw()
		self.set_axes()

if __name__ == '__main__':
	gui = Show_GUI()




