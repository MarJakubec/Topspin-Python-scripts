"""
Read me
This is a simple python script for automated collection of 2H spectra for 
barriers related experiment. 

Installation
Copy text of this script into user python folder (command "edpy") in Topspin. 
Save as auto_2H.py. Start this script from the command line by writing its 
full name: auto_2H.py

How to use this script
All experimental datasets need to be prepared before running this script. All 
the experiments in a series need to have an increasing number of expno without
gaps. The stock also needs to be measured for each new series. Also, tubes 
need to be in increasing position in sample jet rack (except for stock). You 
need to be in the folder you are running the experiment. Afterwards, it is 
possible to start this script (“auto_2H.py”). 
"""

# import expno position
curdat = CURDATA()

# Input - stock and first expno of series
start = INPUT_DIALOG("Amazing automation from Martin",\
"Starting parameters input",
["Position of STOCK tube= ","Position of FIRST tube =",\
"NEXPO of first experiment =","Length of series (including STOCK)="],\
["101","102","1","7"], ["","","",""], ["1","1","1","1"])

rep = int(start[3])
sta = int(start[2])
postock = int(start[0])
possam = int(start[1])
# print of commands
for x in range(rep):
	if x==0: 
		XCMD("re "+str(sta))
		SLEEP(1)
		XCMD("qu sx "+str(postock))
		XCMD("qu lock h2o+d2o")
		XCMD("qu topshim 2h")
		XCMD("qu zg")
	else:
		XCMD("re "+str(sta+x))
		SLEEP(1)
		XCMD("qu sx "+str(possam+x-1)) 
		XCMD("qu zg")
