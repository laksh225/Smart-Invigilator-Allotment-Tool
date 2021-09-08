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

from faculty import increment_flag
from input import load
from random import choice, sample

fac_dict = {}
fac_dict[0] = load()			# load return a list of faculties
								# Define HoD


def get_faculty(designation, minimum=0, load_all = 0):
	fac_list = []
	global fac_dict
	for key, _ in fac_dict:
		while(key<minimum):
			key+=1
			continue
		if (load_all):
			fac_list.append(lambda fac:fac.designation==designation, fac_dict[key])
		else:
			while(1):
				fac_list.append(fac_dict[key])
	return fac_list
		
def random_unique(rep, added_list, designation):
	unique_list = []
	for i in range(1000):
		if designation=="Professor":
			fac = choice(p_list)
		elif designation=="Associate Professor":
			fac = choice(asop_list)
		elif designation=="Assistant Professor":
			fac = choice(assp_list)
		else:
			raise Exception(f'Designation {designation} does not exist')
		if fac not in unique_list:
			if fac not in added_list:
				unique_list.append(fac)
				change_list(fac, designation)
				changeifempty(designation)
			if len(unique_list) == rep:
				break
		if i==999:
			print("Not enough staff")
			print(unique_list, added_list)
	return unique_list
	
def random_unique(rep, added_list, designation):
	try:
		fac_list = get_faculty(designation)
	except:
		raise Exception(f'Designation {designation} does not exist')
	fac_list = filter(lambda fac:fac not in added_list, fac_list)
	#add case if fac_list is empty and fac_list has length less than rep
	unique_list = sample(fac_list, rep)
	return unique_list
	
class Allocation:
	def __init__(self):
		self.sessions = [[] for i in range(1+6)] # Staff same for all 6 sessions plus session wise staff allocation
		
	def __str__:
		print(self.sessions)
		
	def allocate(n):
		DySp = random_unique(1, session[0], "Professor")
	increment_flag(DySp)
	print(f'\nDEPUTY SUPERINTENDENT = {DySp}\n')

	invigilators = random_unique(10, squad+ \
	session[1]+session[2]+session[3], "Assistant Professor")
	increment_flag(invigilators)
	print(f'INVIGILATORS = {invigilators}\n')

	backup = random_unique(3, squad+ \
	session[1]+session[2]+invigilators+session[3], "Assistant Professor")
	increment_flag(backup)
	print(f'BACKUP = {backup}\n')

	reliever = random_unique(3, session[4], "Associate Professor")
	increment_flag(reliever)
	print(f'RELIEVER = {reliever}\n')

	assert(len(set(squad+invigilators+backup))== \
	len(squad+invigilators+backup))
	session2 = [DySp]+[squad]+[invigilators]+[backup]+[reliever]
	self.sessions[n] = session2
	
	def allocate_special():
	#Squad
	#HoD
	squad = random_unique(4, session[1]+session[2]+session[3], "Assistant Professor")
	increment_flag(squad)
	print(f'SQUAD = {squad}\n')
	
	global HoD
	print(f'HoD = {HoD}')
	self.sessions
		
def main():
	session0 = [[],[],[],[],[]]
	
	print("\n*****************Session 1***********************\n")
	session1 = allocate(session0)
	
	print("\n*****************Session 2***********************\n")
	session2 = allocate(session1)

	print("\n*****************Session 3***********************\n")
	session3 = allocate(session2)
	print("\n*****************Session 4***********************\n")
	session4 = allocate(session3)
	print("\n*****************Session 5***********************\n")
	session5 = allocate(session4)
	print("\n*****************Session 6***********************\n")
	session6 = allocate(session5)
	
	sessions = [session1]+[session2]+[session3]+[session4]+[session5]+[session6]
	return sessions
 

if __name__ == '__main__':
	sessions = main()

##############
""" Sessions = List of session
	Session = List of combination of DySp, Squad, Invigilator, Backup, Reliever
	Invigilator = List of faculty objects
"""
