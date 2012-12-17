#!/usr/bin/python
######################################
#
#  dbparser.py -- parses output of mysqldump --all-databases
#                 for a specified database (DBNAME) and
#                 outputs the sql code for that database
#
#  Author: Ryan Murphy <ryan.murphy@rychannel.com>
#  Date: 12-17-2012
######################################



inputFile=open('mysqldump.dump','r')

DBNAME="database"

record=False
for line in inputFile.readlines():
    splitLine=line.split()
    #print splitLine
    if len(splitLine)>=3:
        if splitLine[1]=='Current' and splitLine[2]=='Database:':
            if splitLine[3]=="`"+DBNAME+"`":
                record=True

    if len(splitLine)>1 and splitLine[1]=='Current' and record and splitLine[3]!='`'+DBNAME+'`':
        record=False
        inputFile.close()

    if record:
        print line
inputFile.close()
