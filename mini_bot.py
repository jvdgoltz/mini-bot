import time 

import Adafruit_PCA9685

def load_calib(id=0, calib_dir=None):
	pass


class MiniBot():
	def __init__(self, address=0x40, n_servos=5, calib_dir=None):
		#import calibration files for every servo in calib_dir
		#initialize the pwm controller
		self.default_state = None
		self.safe_state = None
		self.i2c_address = address

	def init(self):
		#set joints to default starting position
		pass

	def test_all_joints(self):
		#test all servos after each other to full range
		#then go to default state		
		pass

	def shutdown(self):
		# put joints into safe state 
		pass

	def set_as_default(self, joint_states=None):
		pass

	def set_joint_states(self, joint_states):
		pass

	def get_joint_states(self):
		pass

	def set_ee_pose(self, pose):
		pass

	def get_ee_pose(self):
		pass

	def close_claw(self):
		pass

	def open_claw(self):
		pass

	def set_claw(self, claw_pos):
		pass

def main():
	bot = MiniBot(0x41, n_servos=5, calib_dir="../servos") 
	return 0

if __name__ == '__main__':
	main()
