# Dependencies
import os
import csv

# Specify the file to write to
csvpath = os.path.join("../Resources", "budget_data.csv")

#Open csvpath reading every row
with open(csvpath, newline='') as csvfile:

#Delimiter is comma because csv is seperated by ,
	reader = csv.reader(csvfile, delimiter = ",")

#next will read the next row after row 1
	csv_header = next(csvfile)
	print(f'Header: {csv_header}')

#PyBank
	months=0
	total=0
	maxnumber=0
	minnumber=1000000000000
	for row in reader:
		months += 1
		total += int(row[1])
		if int(row[1]) > int(maxnumber):
			maxnumber = row[1]
		if int(row[1]) < int(minnumber):
			minnumber = row[1]
	print(f'Financial Analysis')
	print(f'__________________________________________')
	print(f'Total Months : {months}')
	print(f'Total Profit/Losses : ${total}')
	print(f'Your largest growth : ${maxnumber}')
	print(f'Your largest decline : ${minnumber}')
# How do I formalize numbers? Add commas and .00?
# How to connect local repo and online repo?
# How to print the analysis to the terminal and
# export a text file with the results.