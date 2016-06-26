#import modules
import csv
from types import *

#initialize input variables
basefilename = 'Jacob Laser 05-09-16'
nlines = 37
nisotopes = 13
scanrate = 10
#times should be set halfway between the time of interest and the time before/after to ensure robust 
#inclusion of the data
starttime = 0.0 
endtime = 1000.0

#initialize filelist from base name and number of lines assumes name structure 'basename_number.csv'
filelist = []
for i in range(1,nlines+1):
	filelist.append(basefilename + '_' + str(i) + '.csv')

#read file data into list 'raw'
raw = [[] for i in range(0,nlines)]
inheaders = [[]]
a = 0
for i in filelist:
	with open(i) as csvfile:
         	reader = csv.reader(csvfile)
        	for row in reader:
			#extract column titles from first file to reuse in output
			if reader.line_num == 14 and (a == 0):
				inheaders[0] = row
       			#if the value in the first column is a float save the row to the data array to 
			#robustly extract data
			if len(row) > 0:
				try:
                       			float(row[0])
                       			val = True
               			except ValueError:
                       			val = False
               			if val and float(row[0]) > starttime and float(row[0]) < endtime:
                      				raw[a].append(row)
	a = a+1

#imported  is in rows by file: row[i] is file and row[i][j] is a row in that file
#this is converted to columns in data: each data[i] is a column, data[i][j] is the value in the jth row
#columns are grouped: 1-nlines columns of time, then 1-nlines columns of isotope 1, etc
#manipulations should be done while data is in this structure
data = [[] for i in range(0,(nisotopes+1)*nlines)]
for j in range(0,nlines):
	for i in range(0,nisotopes+1):
		for k in range(0,len(raw[j])):
			data[j+i*(nlines)].append(raw[j][k][i])

#determine the length of the longest column for arraying/iterating
rows = 0
for i in range(0,len(data)):
	if len(data[i]) > rows:
		rows = len(data[i])

#convert time columns to distance using scan rate and d=r*t
#to leave as time comment out this section
inheaders[0][0] = 'Position'
for i in range(0,nlines):
	for j in range(0,len(data[i])):
		data[i][j] = scanrate*float(data[i][j])

#create header list to make data easier to interpret using the titles from input data 
header = [[]]
header[0].append(inheaders[0][0]) 
a = 1
for i in range(37,(nisotopes+1)*(nlines)):
	if (i%37)+1==1:
		header[0].append(inheaders[0][a]) 
		a = a+1
	else:
		header[0].append('') 

#return the collected data to row form for writing
#only prints last time column to print all set the lower limit of the range to zero
#to fix titles to match change simply delete the row 'header[0].append(inheaders[0][0])' and set a = 0
output = [[] for i in range(0,rows)]
for i in range(36,len(data)):
	for j in range(0,rows):
		if j < len(data[i]):
			output[j].append(data[i][j])
		else:
			output[j].append('')
	
#write new data to csv named 'output.csv'
with open('output.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(header)
   	writer.writerows(output)

