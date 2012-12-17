#!/usr/bin/python

###############################
#
# permcheck.py -- Takes in a list of drupal sites
#                 based on file directory location,
#                 not web location, and returns their 
#                 anonymous user permissions
#				  Only returns output if anonymous
#                 user has Edit or Create permission.
#
# Author:Ryan Murphy <ryan.murphy@rychannel.com>
# Date: 12-17-2012
###############################


"""Import Python Modules"""
import os
import subprocess

"""Giving a module an alias so its easier to use"""
import MySQLdb as mdb


"""Open file with list of sites dirs"""
inputFile = open('drupal6sites.txt','r')


"""Read through each line"""
for line in inputFile.readlines():
	"""Remove \n from each line"""
	directory = line.rstrip("\n")
	
	"""Change Current Working Directory to site directory"""
	os.chdir(directory)
	
	"""Run Drush Status on each site"""
	proc = subprocess.Popen(["drush status"], stdout=subprocess.PIPE, shell=True)
	out,err = proc.communicate()

	"""Remove all that pesky whitespace"""
	out=out.replace(' ','')
	out=out.split("\n")
	
	"""Split each required field into its own list"""
	try:
		out[3]=out[3].split(':')
		out[5]=out[5].split(':')
	except:
		continue
	"""Grab the data out of the mini lists"""
	dbserver=out[3][1]
	dbname= out[5][1]
	
	print directory
	print "Connecting to "+dbname+" on "+dbserver+"..."

	"""Connect to the respective Mysql DB"""
	con = None
	try:
		con = mdb.connect(dbserver,'root','password',dbname)
		cur = con.cursor()
		cur.execute("SELECT * FROM permission WHERE rid=1")

		data = cur.fetchone()
		if data==None:
			continue
		data = data[2]

		print data
		if "edit" in data or "create" in data:
			print "EDIT/CREATE PERMISSION DETECTED"

		cur2 = con.cursor()
		cur2.execute("SELECT * FROM users_roles WHERE uid=0")

		data = cur.fetchone()
		if data != None:
			print "ALERT, MULTIPLE ROLES DETECTED"
			print data

	except mdb.Error, e:
		print "MYSQL ERROR-- RED ALERT!!! -- "+str(e.args[0])+" "+str(e.args[1])
	
	finally:
		if con:
			con.close()
	print
