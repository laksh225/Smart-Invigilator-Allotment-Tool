from time import sleep
from faculty import increment_flag, Faculty
from input import load
from random import sample

fac_dict = {}
fac_dict[0] = load()			# load return a list of faculties
HoD = [Faculty(100, "Dr. K S Geetha", 0, "HoD", 1)]					# Get HoD


def get_faculty(designation, load_all = 0):
	fac_list = []
	global fac_dict
	for flag in fac_dict.keys():
		#if (load_all):
		fac_list+=list(filter(lambda fac:fac.designation==designation, [fac for facl in fac_dict[flag] for fac in facl]))
		#else:
		#	while(1):
		#		fac_list+=fac_dict[flag]
	return fac_list

def random_unique(rep, added_list, designation, experience=0):
	fac_list = get_faculty(designation)
	if len(fac_list)==0:
		print("Empty fac_list was returned")
		sleep(1)
	fac_list = list(filter(lambda fac:fac not in added_list, fac_list))
	if experience:
		fac_list = list(filter(lambda fac:fac.experience==1, fac_list))
	if len(fac_list)==0 or len(fac_list)<rep:
		if not load_all:
			return random_unique(rep, added_list, designation, load_all=1)
		else:
			return Exception("Enough staff not available")
	unique_list = sample(fac_list, rep)
	return unique_list

class Allocate:
	def __init__(self):
		self.sessions = [[] for i in range(1+6)] # Staff same for all 6 sessions plus session wise staff allocation

	def __str__(self):
		print(self.sessions)

	def allocate(self, n):
		comman = self.sessions[0][0]+self.sessions[0][1]
		DySp = random_unique(1,self.sessions[n-1][0]+comman, "Professor")
		increment_flag(DySp)
		print(f'\nDEPUTY SUPERINTENDENT = {DySp}\n')

		invigilators = random_unique(10, self.sessions[n-1][1]+self.sessions[n-1][2]+comman, "Assistant Professor")
		increment_flag(invigilators)
		print(f'INVIGILATORS = {invigilators}\n')

		backup = random_unique(3, invigilators+self.sessions[n-1][1]+\
			self.sessions[n-1][2]+comman, "Assistant Professor")
		increment_flag(backup)
		print(f'BACKUP = {backup}\n')

		reliever = random_unique(3, self.sessions[n-1][3], "Associate Professor")
		increment_flag(reliever)
		print(f'RELIEVER = {reliever}\n')

		assert(len(set(invigilators+backup))== \
		len(invigilators+backup))
		self.sessions[n] = [DySp]+[invigilators]+[backup]+[reliever]

	def allocate_comman(self):
		squad = random_unique(4, [], "Assistant Professor", experience = 1)
		increment_flag(squad)
		print(f'SQUAD = {squad}\n')

		global HoD
		increment_flag(HoD)
		print(f'HoD = {HoD}')
		self.sessions[0]=[squad]+[HoD]+[[]]+[[]]+[[]]+[[]]	#Empty list added so that allocate does not throw error for first session
		print(self.sessions)

def main():
	sessions = Allocate()
	sessions.allocate_comman()
	print("\n*****************Session 1***********************\n")
	sessions.allocate(1)
	print("\n*****************Session 2***********************\n")
	sessions.allocate(2)
	print("\n*****************Session 3***********************\n")
	sessions.allocate(3)
	print("\n*****************Session 4***********************\n")
	sessions.allocate(4)
	print("\n*****************Session 5***********************\n")
	sessions.allocate(5)
	print("\n*****************Session 6***********************\n")
	sessions.allocate(6)

	return sessions


if __name__ == '__main__':
	sessions = main()

##############
""" Sessions = List of session
	Session = List of combination of DySp, Squad, Invigilator, Backup, Reliever
	Invigilator = List of faculty objects
"""

"""Model 1
400 students 10 classroom
Rvce ECE staff structure
HOD-1 (CS)
Prof-5(DSP)
Associate prof- 10(rel/squad)
Assist prof-35(squa/rs)

Inputs-
•	 Excel sheets
•	 Gender
•	 Designation names
•	 Experience(Hi/Lo)
Number of days number of shifts
Previous exam history.
Computation:
Creating variables
Level 1:
Random selection:
•	 1 out of 5 - prof
•	 Squad 4 (2 +2) out of 35 ast p
•	 10 out of 31-astp
•	 3 out of 10-aso P
•	 HOD
•	 Backup 3out of 21 astp
Level 2					  //Afternoon Session
Module sel
No rep selection:
•	 10 out of 21-astp
•	 3 out of 7-aso P
•	 1out of 4- prof
•	 3 out of 11
Level 3
10 out of 21
3 out of7
1 out of 4
3 out 11

Flag
•	 Random selection of AP, P, ASSpof
•	 If duty then duty=duty+1

Range 1-5 Professors
6-14 Associate
15-48 Assistant
"""

