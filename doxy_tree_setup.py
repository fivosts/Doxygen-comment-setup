#!/usr/bin/python2

import subprocess, os
import sys

def generate(item, prev_path):
	print prev_path  + item
	print os.path.isdir(prev_path+item)
	print os.listdir(prev_path+item)
	if os.path.isfile(item):
		#split it to find if it is C
		#go and modify it
		pass
	elif os.path.isdir(item):
		print os.listdir(item)
		for dir in os.listdir(item):
			generate("/"+os.listdir(item)[0], prev_path+item)


	return

if __name__ == '__main__':

	dir_list = sys.argv
	del dir_list[0]
	if os.path.basename(__file__) in dir_list: 
		dir_list.remove(os.path.basename(__file__))
	# for i in range(1, len(sys.argv)):
		# if 
		# dir_list.append(sys.argv[i])
		# print sys.argv[i]

	for item in dir_list:
		if item[-1] == "/":
			item = item[:-1]
		generate(item, "")