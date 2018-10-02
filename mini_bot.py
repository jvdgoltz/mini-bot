import time 

import Adafruit_PCA9685
import utils

def load_calib(n_servos, calib_dir=None):
    if calib_dir is None:
        calib_dir = 'servo_calib'
    calib = []
    for id in range(n_servos):
        calib.append(utils.read_calib(calib_dir+"/{}".format(id)))
    return calib
    
def deg2pulse(angles, calib):
	pulse = angles
	for i in range(len(angles)):
		if angles[i]<calib[i]['max_deg'] and angles[i]>calib[i]['min_deg']:
			pulse[i] = int(round(calib[i]['m']*angles[i]+calib[i]['c']))
		else:
			print('WARNING: invalid servo angle requested!')
			pulse[i] = int(round(max(min(calib[i]['m']*angles[i]+calib[i]['c'],calib[i]['max']),calib[i]['min'])))
	return pulse

class MiniBot():
	def __init__(self, address=0x40, busnum=None, n_servos=6, calib_dir=None):
		#import calibration files for every servo in calib_dir
		#initialize the pwm controller
		self.n_servos = n_servos
		self.default_angles = [0,0,0,0,0,0]
		self.safe_angles = None
		self.pwm = Adafruit_PCA9685.PCA9685(address=address, busnum=busnum)
		self.calib = load_calib(n_servos=n_servos,calib_dir=calib_dir)
		self.set_joint_angles(self.default_angles)

	def test_all_joints(self):
		#test all servos after each other to full range
		#then go to default state		
		pass

	def shutdown(self):
		# put joints into safe state 
		self.set_joint_angles(self.safe_angles)
		pass

	def set_as_default(self, joint_angles=None):
		if joint_angles is None:
			self.default_angles = self.joint_angles
		else:
			self.default_angles = joint_angles 

	def set_joint_angles(self, joint_angles):
		self.joint_angles = joint_angles
		pulses = deg2pulse(joint_angles, self.calib)
		self.set_pwm(pulses)

	def get_joint_angles(self):
		return self.joint_angles

	def set_ee_pose(self, pose):
		pass

	def get_ee_pose(self):
		return self.ee_pose

	def close_claw(self):
		self.set_claw(self.calib[-1]['min_deg'])
		
	def open_claw(self):
		self.set_claw(self.calib[-1]['max_deg'])

	def set_claw(self, claw_angle):
		self.joint_angles[-1] = claw_angle
		pulse = int(round(deg2pulse([claw_angle], [self.calib[-1]])
		self.pwm.set_pwm(self.n_servos-1, 0, pulse)
	
	def set_pwm(self, pulses):
		for i in range(self.n_servos):
			self.pwm.set_pwm(i, 0, pulses[i])

def main():
	bot = MiniBot(0x41, n_servos=6, calib_dir="servo_calib") 
	bot.open_claw()
	time.sleep(1)
	bot.close_jaw()
	return 0
	

if __name__ == '__main__':
	main()
