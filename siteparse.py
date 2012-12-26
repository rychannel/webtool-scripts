#!/usr/bin/python

####################################
#
# siteparse.py -- Opens a text file
#                 containing a list of sites that have
#                 a certain module installed, then 
#                 parses out the site directories.
#
# Author: Ryan Murphy <ryan.murphy@rychannel.com>
# Date: 12-16-2012
#
# Note: Needs a better name
#				  
####################################



"""Open the file to be parse"""

inputFile = open('panelsites.txt','r')

"""Create a list for the site directories"""
sitedirs=[]

""" Loop through each line of the file"""
for line in inputFile.readlines():

	"""Find the actual site directories and add them to the list"""
	if line[0]=="/":

		"""Strip \n from the end of each line"""
		line=line.strip("\n")

		sitedirs.append(line)
		print line

"""Close the file"""
inputFile.close()
