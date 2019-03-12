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
	allvote = {"Khan":K, "Correy":C,"Li":L,"O'Tooley":O}
	maximum = max(allvote, key=allvote.get)
	print(f'Election Results')
	print(f'____________________________________')
	print(f'Total Votes: {votecount}')
	print(f'____________________________________')
	print(f'Khan received {K} votes ({int(K/votecount*100)}%)')
	print(f'Correy received {C} votes ({int(C/votecount*100)}%)')
	print(f'Li received {L} votes ({int(L/votecount*100)}%)')
	print(f'OTooley received {O} votes ({int(O/votecount*100)}%)')
	print(f'Winner is ... {maximum}')
	print(f'____________________________________')

	text_file = open("output.txt","w")
	text_file.write(f'Election Results\n')
	text_file.write(f'____________________________________\n')
	text_file.write(f'Total Votes: {votecount}\n')
	text_file.write(f'____________________________________\n')
	text_file.write(f'Khan received {K} votes ({int(K/votecount*100)}%)\n')
	text_file.write(f'Correy received {C} votes ({int(C/votecount*100)}%)\n')
	text_file.write(f'Li received {L} votes ({int(L/votecount*100)}%)\n')
	text_file.write(f'OTooley received {O} votes ({int(O/votecount*100)}%)\n')
	text_file.write(f'Winner is ... {maximum}\n')
	text_file.close()