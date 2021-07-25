"""Model 1
400 students 10 classroom
Rvce ECE staff structure
HOD-1 (CS)
Prof-5(DSP)
Associate prof- 10(rel/squad)
Assist prof-35(squa/ rs)

Inputs- 
•    Excel sheets
•    Gender
•    Designation names
•    Experience(Hi/Lo)
Number of days number of shifts
Previous exam history.
Computation:
Creating variables
Level 1:
Random selection: 
•    Squad 4 (2 +2) out of 35
•    10 out of 31-astp
•    3 out of 10-aso P
•    1out of 5- prof
•    HOD
•    Backup 3out of 21 astp
Level 2
Module sel
No rep selection:
•    10 out of 21-astp
•    3 out of 7-aso P
•    1out of 4- prof
•    3 out of 11
Level 3
10 out of 21
3 out of7
1 out of 4
3 out 11

Flag
•    Random selection of AP, P, ASSpof
•    If duty then duty=duty+1

Range 1-5 Professors
6-14 Associate
15-48 Assistant
"""

from faculty import increment_flag
from input import load
import random

fac_list = load()
#print(fac_list)
#days = input("Enter of days")
#shifts =  input("Enter no. of shifts")
DySp = []
for i in range(1):
    index = random.randint(1-1, 5-1)
    #print([fac for fac in fac_list if fac.index==index])
    DySp.append(fac_list[index])
increment_flag(DySp)
#print(set(DySp))

def random_unique(start, stop, rep):
    unique_list = []
    while(True):
        index = random.randrange(start, stop)
        if index not in unique_list:
            unique_list.append(index)
            if len(unique_list) == rep:
                break
    return unique_list

squad = random_unique(15-1, 48-1, 4)
increment_flag([fac_list[fac] for fac in squad])
print([fac_list[fac] for fac in squad])

