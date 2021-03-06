from matplotlib.widgets import Slider, RadioButtons, Button
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from joint import Joint
import math
import forwardKinematics as fK
from ipywidgets import widgets

# This class performs all the GUI handling and interfaces with the back
# end to compute new joint positions.
class Show_GUI():

	def __init__(self, filename):

		self.filename = filename

		# Initialize all the variables
		self.fig = plt.figure("DH Parameters	Robot Simulator")  #create the frame
		self.axes = plt.axes([0.05, 0.25, 0.90, 0.75], projection='3d')
		# Ensures that autoscaling is off
		self.axes.autoscale(enable=False,axis='both')

		# Starts with a default of 4 joints.
		self.numJoints = 4

		# Initialize all the joints
		jointInit = Joint(1, 0)
		jointInit.setCoordSys()
		self.joints = [jointInit]

		for i in range(1, self.numJoints):
			joint = Joint(1,i)
			joint.initJoint = jointInit
			self.joints.append(joint)

		self.joints[0].setCoordSys()
		self.currentJoint = self.joints[1]

		def update_link():
			curID = self.currentJoint.ID
			while curID < self.numJoints:
				oldJoint = self.joints[curID - 1]
				curJoint = self.joints[curID]

				curJoint.defineNew(oldJoint)
				curID += 1

			self.drawJoints()

		update_link()


		# Here, we create the interactive elements of the plot

		# Draw Theta slider panel
		thetaVals = plt.axes([0.35, 0.20, 0.30, 0.03])
		self.theta_slide = Slider(thetaVals, 'Theta Value', -180, 180, valinit=math.degrees(self.currentJoint.theta))
		
		# Draw d slider panel
		dVals = plt.axes([0.35, 0.1575, 0.30, 0.03])
		self.d_slide = Slider(dVals, 'D Value', 0.0, 10, valinit=self.currentJoint.d)

		# Draw r slider panel
		rVals = plt.axes([0.35, 0.115, 0.30, 0.03])
		self.r_slide = Slider(rVals, 'R Value', 0.0, 10, valinit=self.currentJoint.r)

		# Draw Alpha slider panel
		alphaVals = plt.axes([0.35, 0.0725, 0.30, 0.03])
		self.alpha_slide = Slider(alphaVals, 'Alpha Value', -180, 180, valinit=math.degrees(self.currentJoint.alpha))

		# Link selection slider
		linkNum = plt.axes([0.35, 0.03, 0.30, 0.03])
		self.link_slide = Slider(linkNum, 'Link Number', 1, self.numJoints-1, valinit=1, valfmt='%0.0f', )

		# Create radio button for joint type.
		jointType = plt.axes([0.75, 0.040, 0.15, 0.12])
		jointType.set_title('Joint Type', fontsize=12)
		types = {'Prismatic': 0, 'Revolute': 1}
		self.jointOptions = RadioButtons(jointType, types.keys(), active=1)

		# Button for forward kinematics map
		fKButton = plt.axes([0.05, 0.15, 0.11, 0.06])
		fKGenerate = Button(fKButton, 'Fwd Kinem.')

		# Button for adding a joint
		addButton = plt.axes([0.05, 0.05, 0.11, 0.06])
		addJoint = Button(addButton, 'Add Joint')


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

		def generateMap(val):
			fK.generateFK(self.joints, self.filename)

		# When the link slider is changed, this function is called. 
		# It is responsible for updating the slider values and changing
		# the currentJoint reference.
		def changeCurrentLink(val):
			newVal = int(round(val))
			if newVal != self.currentJoint.ID:
				self.currentJoint = self.joints[int(round(val))]
				self.theta_slide.set_val(math.degrees(self.currentJoint.theta))
				self.d_slide.set_val(self.currentJoint.d)
				self.r_slide.set_val(self.currentJoint.r)
				self.alpha_slide.set_val(math.degrees(self.currentJoint.alpha))
				self.jointOptions.active = self.currentJoint.type

		# This is triggered when the add button is clicked. It intializes a new
		# joint and updates the slider values.
		def addNew(val):
			joint = Joint(1,self.numJoints)
			joint.initJoint = jointInit
			self.joints.append(joint)

			self.numJoints += 1
			self.link_slide.valmax = self.numJoints - 1
			self.link_slide.ax.set_xlim(self.link_slide.valmin, self.link_slide.valmax)
			update_link()

		self.theta_slide.on_changed(getTheta)
		self.d_slide.on_changed(getD)
		self.r_slide.on_changed(getR)
		self.alpha_slide.on_changed(getAlpha)
		self.link_slide.on_changed(changeCurrentLink)

		self.jointOptions.on_clicked(changeType)
		fKGenerate.on_clicked(generateMap)
		addJoint.on_clicked(addNew)

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

	# This function plots coordinate systems on top of the joints so we
	# can better visualize their movements/rotations.
	def plotCoordinateSystem(self):
		for i in range(self.numJoints):
			joint = self.joints[i]
			originCoord = self.joints[0].coordSystem
			coord= joint.coordSystem
			posX = joint.x
			posY = joint.y
			posZ = joint.z
			lineDist = 1
			
			xPoint = coord.locate_new('xPoint', lineDist*coord.i + 0*coord.j + 0*coord.k)
			(xMove,yMove,zMove) = xPoint.origin.express_coordinates(originCoord)
			xs=list((posX,xMove))
			ys=list((posY,yMove))
			zs=list((posZ,zMove))
			self.axes.plot(xs,ys,zs, linewidth = 1, color="green")
			
			yPoint = coord.locate_new('yPoint', 0*coord.i + lineDist*coord.j + 0*coord.k)
			(xMove,yMove,zMove) = yPoint.origin.express_coordinates(originCoord)
			xs=list((posX,xMove))
			ys=list((posY,yMove))
			zs=list((posZ,zMove))
			self.axes.plot(xs,ys,zs, linewidth = 1, color="blue")
			
			zPoint = coord.locate_new('zPoint', 0*coord.i + 0*coord.j + lineDist*coord.k)
			(xMove,yMove,zMove) = zPoint.origin.express_coordinates(originCoord)
			xs=list((posX,xMove))
			ys=list((posY,yMove))
			zs=list((posZ,zMove))
			self.axes.plot(xs,ys,zs, linewidth = 1, color="red")

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

		self.axes.set_xlim3d(-5, 15)
		self.axes.set_ylim3d(-10, 10)
		self.axes.set_zlim3d(0, 10)
		self.axes.set_xlabel('X axis')
		self.axes.set_ylabel('Y axis')
		self.axes.set_zlabel('Z axis')

	def drawJoints(self):
	
		self.plotJoints()
		self.plotCoordinateSystem()
		
		plt.draw()
		self.set_axes()

if __name__ == '__main__':
	filename = "forwardKinematics.csv"
	gui = Show_GUI(filename)




