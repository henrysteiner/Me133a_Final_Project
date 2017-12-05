from matplotlib.widgets import Slider, RadioButtons
import matplotlib.pyplot as plt

# import Joint # CHANGE
# import Link # CHANGE

class Show_GUI():

	def __init__(self):

		self.fig = plt.figure("DH Parameters	Robot Simulator")  #create the frame 
		# Draw Theta slider panel
		thetaVals = plt.axes([0.35, 0.1425, 0.45, 0.03])
		theta_val = Slider(thetaVals, 'Theta Value', 0.0, 180, valinit=90)
		
		# Draw D slider panel
		dVals = plt.axes([0.35, 0.1, 0.45, 0.03])
		d_val = Slider(dVals, 'D Value', 0.0, 300, valinit=0)

		# Draw A slider panel
		rVals = plt.axes([0.35, 0.0575, 0.45, 0.03])
		r_val = Slider(rVals, 'R Value', 0.0, 300, valinit=0)

		# Draw Alpha slider panel
		alphaVals = plt.axes([0.35, 0.015, 0.45, 0.03])
		alpha_val = Slider(alphaVals, 'Alpha Value', 0.0, 180, valinit=90)

		# Create radio button
		joint = plt.axes([0.05, 0.02, 0.15, 0.12])
		joint.set_title('Joint Type', fontsize=12)
		jointOptions = RadioButtons(joint, ('Prismatic', 'Revolute'), active=2)

		def update_theta_val(val):
			# print('theta: ' + str(val))

		theta_val.on_changed(update_theta_val)

		def update_d_val(val):
			# print('d: ' + str(val))

		d_val.on_changed(update_d_val)

		def update_r_val(val):
			# print('r: ' + str(val))

		r_val.on_changed(update_r_val)

		def update_alpha_val(val):
			# print('alpha: ' + str(val))

		alpha_val.on_changed(update_alpha_val)

		plt.show()

	def createJoint(self):
		self.numJoints += 1
		joint = Joint(typeInit, self.numJoints)
		link = Joint(d0, theta0, r0, alpha0, typeInit)
		self.numJoints += 1

gui = Show_GUI()




