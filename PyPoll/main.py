# Dependencies
import os
import csv

# Specify the file to write to
csvpath = os.path.join("../Resources", "election_data.csv")

#Open csvpath reading every row
with open(csvpath, newline='') as csvfile:

#Delimiter is comma because csv is seperated by ,
	reader = csv.reader(csvfile, delimiter = ",")

#next will read the next row after row 1
	csv_header = next(csvfile)
	print(f'Header: {csv_header}')

#PyPoll
	votecount=0
	K = 0
	C = 0
	L = 0
	O = 0
	for row in reader:
		votecount+=1
		if row[2]=="Khan":
			K +=1 
		if row[2]=="Correy":
			C +=1 
		if row[2]=="Li":
			L +=1 
		if row[2]=="O'Tooley":
			O +=1 

	print(f'Election Results')
	print(f'____________________________________')
	print(f'Total Votes: {votecount}')
	print(f'____________________________________')
	print(f'Khan received {K} votes ({K/votecount}%)')
	print(f'Correy received {C} votes ({C/votecount}%)')
	print(f'Li received {L} votes ({L/votecount}%)')
	print(f'OTooley received {O} votes ({O/votecount}%)')
	print(f'Winner is ...')
	print(f'____________________________________')

