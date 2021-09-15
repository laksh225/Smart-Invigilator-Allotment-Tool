from time import sleep
from faculty import Faculty, inc_flag
from input import load
from random import shuffle


fac_dict = {}
fac_dict[0] = load()			# load return a list of faculties
HoD = [Faculty("Dr. K S Geetha", 0, "HoD", 1, 1)]					# Get HoD

def get_faculty(designation, index, load_all = 0):
	fac_list = []
	global fac_dict
	#if (load_all):
	fac_list=list(filter(lambda fac:fac.designation==designation, fac_dict[index]))
	#else:
	#	while(1):
	#		fac_list+=fac_dict[flag]
	return fac_list

def random_unique(rep, added_list, designation, experience=0):
	unique_list = []
	i = 0
	while(len(unique_list)<rep):
		fac_list = get_faculty(designation, i)
		fac_list = list(filter(lambda fac:fac not in added_list, fac_list))
		if experience:
			fac_list = list(filter(lambda fac:fac.experience==1, fac_list))
		if i>=1000:
			raise Exception("Enough staff not available")
		shuffle(fac_list)
		unique_list += fac_list
		i+=1
	return unique_list[0:rep]

class Allocate:
	def __init__(self):
		self.sessions = [[] for i in range(1+6)] # Staff same for all 6 sessions plus session wise staff allocation

	#def __str__(self):
	#	print(self.sessions)

	def allocate(self, n):
		comman = self.sessions[0][0]+self.sessions[0][2]
		DySp = random_unique(1,self.sessions[n-1][0], "Professor")
		[fac.inc_flag() for fac in DySp]
		print(f'\nDEPUTY SUPERINTENDENT = {DySp}\n')

		invigilators = random_unique(10, self.sessions[n-1][1]+comman, "Assistant Professor")
		[fac.inc_flag() for fac in invigilators]
		print(f'INVIGILATORS = {invigilators}\n')

		reliever = random_unique(3, self.sessions[n-1][2], "Associate Professor")
		[fac.inc_flag() for fac in reliever]
		print(f'RELIEVER = {reliever}\n')

		self.sessions[n] = [DySp]+[invigilators]+[reliever]

	def allocate_comman(self):
		backup = random_unique(3, [], "Assistant Professor")
		print(f'BACKUP = {backup}\n')

		squad = random_unique(4, backup, "Assistant Professor", experience = 1)
		for fac in squad:
			fac.flag+=3
		print(f'SQUAD = {squad}\n')

		global HoD
		HoD[0].flag+=1						#What to put?
		print(f'HoD = {HoD}')
		self.sessions[0]=[squad]+[HoD]+[backup]+[[]]+[[]]+[[]]	#Empty list added so that allocate does not throw error for first session
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
	print(sessions.sessions)

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

