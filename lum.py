infilename = 'h20-lifetime-raw-dil.csv'
outfilename = 'output.csv'

#import modules
import csv
from types import *

#initialize variables
data = []
time = []
average = [None]*501
reindex = [None]*501*28
rows = [['Time (ms)', 'Average', 'Replicates:',2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]]

#read data ignoring parameters and labels
with open(infilename) as csvfile:
	reader = csv.DictReader(csvfile, fieldnames=['time', 'intensity'])
	##if the value in the first column is a float
	##save both values to the data file to robustly extract data
	for row in reader:
		try:
			float(row['time'])
			val = True
		except ValueError:
			val = False
		if val: 	
			time.append(float(row['time']))
			data.append(float(row['intensity']))

#reindex data to be in columns by repitition
#EXPECTS 25 REPITITIONS AND 501 DATA POINTS/REP (0.04ms step from 0-20 ms)
for j in range(2,27):
	for i in range(0,501):
		reindex[i*27+j] = data[i+(j-2)*501]

#calculates the average of each row
for i in range(1,502):
	lower = 2+27*(i-1)
	upper = i*27
	average[i-1] = sum(reindex[lower:upper]) / 25

#add times and averages to the first two columns
for i in range(0,501):
	reindex[i*27] = time[i]	
	reindex[i*27+1] = average[i]

#prepare rows for writing to CSV
for i in range(1,502):
	rows.append(reindex[(i-1)*27:i+i*26])

#write to file
with open(outfilename,'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerows(rows)

