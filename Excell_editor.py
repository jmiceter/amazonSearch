# Module: Excell_editor.py
#"D:/Projects/JXM Products, llc/amazon filter/Excell_editor.py"
# FUNCTIONS
#
# initialize CSV aka open and read CSV
# set up the current CSV in list form parse into a list and send
# recieve a list and parse into a CSV file for easy reading. close the CSV
#
import time
import datetime

import csv

appVersion = "1.02.000"

def realStartSearch():
	#open stored csv file
	RankingFile = open('Top100_Ranking.csv','r+')
	RankingFile.readline() # read over the top header file
	FileEditer = csv.writer(RankingFile)

	# common_list will hold the item list
	common_list = RankingFile.readlines()
	for x in range(len(common_list)):
	    print(common_list[x])

	# append a row and save the CSV
	hello = ['hello', 'world', 'what' ,'','line' ,'','','', 'is this']
	FileEditer.writerow(hello)
	RankingFile.close()

def StartSearch():
	print("opening list")
	date = TimeStamp()
	print(date)
	print("Version" + appVersion)
	CloseSearch()

def CloseSearch():
	print("search ended")

# Helper function:
# Provide timestamp for log file.
def TimeStamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%m/%d/%Y %H:%M:%S')
    return st