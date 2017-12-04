class Link(object):
	'''This class establishes a link, whether prismatic or revolute'''
	def __init__(self,d,theta,r,alpha,type):
			self.r = r
			self.alpha = alpha
		if type == 1: #  0 for prismatic, 1 for revolute
			self.theta = theta
			self.d = d
		else:
			self.d = theta
			self.theta = 0







