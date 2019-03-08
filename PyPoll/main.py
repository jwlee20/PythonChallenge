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
	print(f'Khan received {K} votes ({int(K/votecount*100)}%)')
	print(f'Correy received {C} votes ({int(C/votecount*100)}%)')
	print(f'Li received {L} votes ({int(L/votecount*100)}%)')
	print(f'OTooley received {O} votes ({int(O/votecount*100)}%)')
	print(f'Winner is ...')
	print(f'____________________________________')

